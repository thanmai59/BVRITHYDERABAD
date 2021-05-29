import csv

labels = ['ID', 'Message', 'NS', 'NNS']
filenames = ["BinaryLabeling.csv", "StrongNeutralLabeling.csv",
             "WeakNeutralLabeling.csv", "IntermediateLabeling.csv",
            "PartitionsLabeling.csv"]
fileobjs = [open("LabeledData/" + i, "r") for i in filenames]
readers = [csv.reader(i) for i in fileobjs]

from nltk.tokenize import word_tokenize
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy
from collections import Counter

# Create featureset from all individual words in training
next(readers[0], None)
num_train = 900 # Training comes from first 900 of 1000 samples
all_words = set()
for row in readers[0]:
    if num_train <= 0:
        break;
    line = word_tokenize(row[1])
    for word in line:
        all_words.add(word)
    num_train -= 1

# Using seek(0) resets reader
fileobjs[0].seek(0)

def bag_of_words(sentence):
    d = dict.fromkeys(all_words, 0)
    c = Counter(word_tokenize(sentence))
    for i in c:
        d[i] = c[i]
    return d

NB_classifiers_NS = []
NB_classifiers_NNS = []
NB_tests_NS = []
NB_tests_NNS = []
for i in readers:
    next(i, None)
    all_data = list(i)
    train_NS = [(bag_of_words(row[1]), row[2]) for row in all_data[:850]]
    train_NNS = [(bag_of_words(row[1]), row[3]) for row in all_data[:850]]
    NB_tests_NS.append([(bag_of_words(row[1]), row[2]) for row in all_data[850:]])
    NB_tests_NNS.append([(bag_of_words(row[1]), row[3]) for row in all_data[850:]])

    NB_classifiers_NS.append(NaiveBayesClassifier.train(train_NS))
    NB_classifiers_NNS.append(NaiveBayesClassifier.train(train_NNS))

for i in range(len(filenames)):
    print(filenames[i])
    print("native speaker:")
    print(accuracy(NB_classifiers_NS[i], NB_tests_NS[i]))
    print("non-native speaker:")
    print(accuracy(NB_classifiers_NNS[i], NB_tests_NNS[i]))
    
import requests
import re
import textstat
import json
import time

# Variables for perspective API call
# headers and parameters for perspective api call
api_key = 'AIzaSyBaMPpybrBfyWF54hvkFK1QuEBPPKmQh8M'
url = ('https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze' +    
    '?key=' + api_key)

# Since readability returns string of form "xth to (x+1)th grade",
# we should only grab the first one.
def find_first_num(s):
    i = re.search('[0-9]+', s).group()
    return int(i)

def features(sentence):
    d = {}
    d['readability'] = find_first_num(textstat.text_standard(sentence))
    d['length'] = len(word_tokenize(sentence))
    
    # preprocessing text to make readable for perspective api scores:
    text = ''
    for a in sentence:
        if a==' ' or (a<='Z' and a>='A') or (a<='z' and a>='a') or (a<='9' and a>='0') or a=='?' or a=='.':
            text +=a

    # perspective api scores call:
    data = '{comment: {text:"'+text+'"}, languages: ["en"], requestedAttributes: {TOXICITY:{}} }'
    response = requests.post(url=url, data=data)
    j = json.loads(response.content)
    # attempting to deal with API issues
    while 'error' in j:
        time.sleep(5)
        response = requests.post(url=url, data=data)
        j = json.loads(response.content)
    try:
        d['toxicity'] = float(j['attributeScores']['TOXICITY']['summaryScore']['value'])
    except:
        d['toxicity'] = 0.0
    assert(len(d.values()) == 3)
    return d

fileobjs[0].seek(0)
# Creating feature dict for each sample in dataset
next(readers[0], None)
all_data = list(readers[0])
feature_data = {}
for row in all_data:
    feature_data[row[0]] = features(row[1])
fileobjs[0].seek(0)

import numpy
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def data_process(num_features):
    # Creating matrix of (samples, features) for sklearn models
    feature_matrix = []
    for i in range(1,1001):
        feature_matrix.append(list(feature_data[str(i)].values()))
    feature_matrix = numpy.array([numpy.array(x) for x in feature_matrix])
    for i in feature_matrix:
        if len(i) != num_features:
            print(i) # debugging in case perspective api fails
    return numpy.stack(feature_matrix, axis=0)

for i in fileobjs:
    i.seek(0)

feature_matrix = data_process(3)

L_classifiers_NS = []
L_classifiers_NNS = []
L_tests_NS = []
L_tests_NNS = []
for i in readers:
    next(i, None)
    list_data = list(i)
    labels_NS = [row[2] for row in list_data]
    labels_NNS = [row[3] for row in list_data]

    # Easier to use DataFrame obj to work with skl models
    data_NS=pd.DataFrame({
        'readability':feature_matrix[:,0],
        'length':feature_matrix[:,1],
        'toxicity':feature_matrix[:,2],
        'politeness': numpy.array(labels_NS)
    })
    data_NS.head()
    data_NNS=pd.DataFrame({
        'politeness': numpy.array(labels_NNS)
    })
    data_NNS.head()
    X=data_NS[['readability', 'length', 'toxicity']]

    # NS training
    # Splitting up into 90% training, 10% verification
    NS_xtrain, NS_xtest, NS_ytrain, NS_ytest = train_test_split(X, data_NS['politeness'], test_size=0.1)
    L_tests_NS.append((NS_xtest, NS_ytest))
    
    # NNS training
    NNS_xtrain, NNS_xtest, NNS_ytrain, NNS_ytest = train_test_split(X, data_NNS['politeness'], test_size=0.1)
    L_tests_NNS.append((NNS_xtest, NNS_ytest))

    clfNS = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0)
    clfNS.fit(NS_xtrain, NS_ytrain)
    clfNNS = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0)
    clfNNS.fit(NNS_xtrain, NNS_ytrain)
    L_classifiers_NS.append(clfNS)
    L_classifiers_NNS.append(clfNNS)

for i in range(len(filenames)):
    print(filenames[i])
    print("native speaker:")
    print(L_classifiers_NS[i].score(L_tests_NS[i][0], L_tests_NS[i][1]))
    print("non-native speaker:")
    print(L_classifiers_NNS[i].score(L_tests_NNS[i][0], L_tests_NNS[i][1]))

