import librosa
import pandas as pd
import numpy as np
import csv
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import keras
from scipy import signal
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestClassifier  
from sklearn.naive_bayes import GaussianNB  
from sklearn.tree import DecisionTreeClassifier  
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import metrics
from tabulate import tabulate
import IPython.display as ipd

header = 'filename zero_crossing_rate_mean zero_crossing_rate_median zero_crossing_rate_std spectral_centroid_mean spectral_centroid_median spectral_centroid_std spectral_contrast_mean spectral_contrast_median spectral_contrast_std spectral_bandwidth_mean spectral_bandwidth_median spectral_bandwidth_std spectral_rolloff_mean spectral_rolloff_median spectral_rolloff_std'
for i in range(1, 21):
    header += f' mfcc_mean{i}'
    header += f' mfcc_median{i}'
    header += f' mfcc_std{i}'
header += ' label'
header = header.split()

genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
def feature_extraction() :
  featurefilename = 'dataset.csv'
  file = open(featurefilename, 'w', newline='')

  with file:
      writer = csv.writer(file)
      writer.writerow(header)
  
  for g in genres:
      for filename in os.listdir(f'C:/Users/Raw/Project/genres/{g}'):
          audio = f'C:/Users/Raw/Project/genres/{g}/{filename}'
          y, sr = librosa.load(audio, mono=True, duration=30)
          zcr = librosa.feature.zero_crossing_rate(y)
          spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
          spec_con = librosa.feature.spectral_contrast(y=y, sr=sr)
          spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
          rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
          
          mfcc = librosa.feature.mfcc(y=y, sr=sr)
          to_append = f'{filename} {np.mean(zcr)} {np.median(zcr)} {np.std(zcr)} {np.mean(spec_cent)} {np.median(spec_cent)} {np.std(spec_cent)} {np.mean(spec_con)} {np.median(spec_con)} {np.std(spec_con)} {np.mean(spec_bw)} {np.median(spec_bw)} {np.std(spec_bw)} {np.mean(rolloff)} {np.median(rolloff)} {np.std(rolloff)}'    
          for e in mfcc:
              to_append += f' {np.mean(e)}'
              to_append += f' {np.median(e)}'
              to_append += f' {np.std(e)}'
          to_append += f' {g}'
          file = open('C:/Users/Raw/Documents/dataset.csv', 'a', newline='')
          with file:
              writer = csv.writer(file)
              writer.writerow(to_append.split())

def data_split() : 
  data = pd.read_csv('C:/Users/Raw/Documents/dataset.csv', error_bad_lines=False)
  data.head()
  data = data.drop(['filename'],axis=1)
  genre_list = data.iloc[:, -1]
  encoder = LabelEncoder()
  y = encoder.fit_transform(genre_list)
  scaler = StandardScaler()
  X = scaler.fit_transform(np.array(data.iloc[:, :-1], dtype = float))
  x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  return (x_train, x_test, y_train, y_test)

def KNN_model(x_train, x_test, y_train) :
  classifier= KNeighborsClassifier(n_neighbors= 3, p = 1)  
  classifier.fit(x_train, y_train)  
  pred = classifier.predict(x_test)  
  return pred

def naive_bayes(x_train, x_test, y_train) :
  classifier = GaussianNB()  
  classifier.fit(x_train, y_train)  
  pred= classifier.predict(x_test)  
  return pred

def decisionTree(x_train, x_test, y_train) : 
  classifier= DecisionTreeClassifier(criterion='entropy', random_state=0)  
  classifier.fit(x_train, y_train)  
  pred= classifier.predict(x_test)  
  return pred

def SVM_model(x_train, x_test, y_train ) :
  classifier = SVC(kernel="linear", random_state=0)  
  classifier.fit(x_train, y_train) 
  pred= classifier.predict(x_test)  
  return pred

def randomForest(x_train, x_test, y_train) : 
  classifier= RandomForestClassifier()  
  classifier.fit(x_train, y_train)  
  pred= classifier.predict(x_test)  
  return pred

def accuracy(y_test, y_pred) : 
  acc = accuracy_score(y_test, y_pred)
  return acc

result = {}

#feature_extraction()

(x_train, x_test, y_train, y_test) = data_split()

knn_pred = KNN_model(x_train, x_test, y_train)
print(knn_pred)
knn_acc = accuracy(y_test, knn_pred)
result['knn'] = knn_acc
print("\naccuracy = ",  knn_acc)
print("\nConfusion matrix")
print(metrics.confusion_matrix(y_test, knn_pred))

nb_pred = naive_bayes(x_train, x_test, y_train)
print(nb_pred)
nb_acc = accuracy(y_test, nb_pred)
result['nb'] = nb_acc
print("\naccuracy = ",  nb_acc)
print("\nConfusion matrix")
print(metrics.confusion_matrix(y_test, nb_pred))

dt_pred = decisionTree(x_train, x_test, y_train)
print(dt_pred)
dt_acc = accuracy(y_test, dt_pred)
result['dt'] = dt_acc
print("\naccuracy = ",  dt_acc)
print("\nConfusion matrix")
print(metrics.confusion_matrix(y_test,dt_pred))

rf_pred = randomForest(x_train, x_test, y_train)
print(rf_pred)
rf_acc = accuracy(y_test, rf_pred)
result['rf'] = rf_acc
print("\naccuracy = ",  rf_acc)
print("\nConfusion matrix")
print(metrics.confusion_matrix(y_test, rf_pred))

svm_pred = SVM_model(x_train, x_test, y_train)
print(svm_pred)
svm_acc = accuracy(y_test, svm_pred)
result['svm'] = svm_acc
print("\naccuracy = ",  svm_acc)
print("\nConfusion matrix")
print(metrics.confusion_matrix(y_test, svm_pred))

result

d = [ ["K Nearesr Neighbours", result['knn']],
      ["Random Forest", result['rf']],
      ["Naive Bayes", result['nb']],
      ["Decision Tree", result['dt']],
      ["Support Vector Machine", result['svm']]]

print(tabulate(d, headers=["Classifier", "Accuracy"]))

def find_genre(audio, classifier) :
  audio_data = audio
  print(audio_data)
  data = pd.read_csv('C:/Users/Raw/Documents/dataset.csv', error_bad_lines=False)
  audio_data = audio_data.split('/')[-1]
  print(audio_data)
  test = data.loc[data['filename'] == audio_data ]
  arr = test.to_numpy()
  arr = np.delete(arr, obj=0, axis=1)
  arr = np.delete(arr, obj=75, axis=1)

  audio_data = audio_data[:-10]
  if(classifier == 'k nearest neighbours') : 
    genre = KNN_model(x_train, arr, y_train)
  if(classifier == 'random forest') : 
    genre = randomForest(x_train, arr, y_train)
  if(classifier == 'naive bayes') : 
    genre = naive_bayes(x_train, arr, y_train)
  if(classifier == 'decision tree') : 
    genre = decisionTree(x_train, arr, y_train)
  if(classifier == 'support vector machine') : 
    genre = SVM_model(x_train, arr, y_train)

  return (audio_data, classifier, genre[0])
"""
original, classifier, predicted = find_genre('C:/Users/Raw/Project/genres/disco/disco.00000.wav', 'support vector machine')
print(original, classifier, genres[predicted])
"""
