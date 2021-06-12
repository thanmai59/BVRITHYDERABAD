# -*- coding: utf-8 -*-


import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
import pandas as pd
data = pd.read_excel('politeness_2k_data.xlsx')
data = data.fillna('_NA_')

label_names = ["target"]
y_train = data[label_names].values

import numpy as np
data['doc_len'] = data['comment'].apply(lambda words: len(words.split(" ")))
max_seq_len = np.round(data['doc_len'].mean() + data['doc_len'].std()).astype(int)

from tqdm import tqdm
import nltk
from nltk.tokenize import word_tokenize


from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", ':', ';', '(', ')', '[', ']', '{', '}'])


## preprocessing starting 
raw_docs_train = data['comment'].tolist()
num_classes = len(label_names)

print("pre-processing train data...")

processed_docs_train = []
for doc in tqdm(raw_docs_train):
    tokens = word_tokenize(doc)
    filtered = [word for word in tokens if word not in stop_words]
    processed_docs_train.append(" ".join(filtered))
    
from tensorflow import keras
from tensorflow.keras.preprocessing import sequence

MAX_NB_WORDS = 10000
from tensorflow.keras.preprocessing.text import Tokenizer


print("tokenizing input data...")
tokenizer = Tokenizer(num_words=MAX_NB_WORDS, lower=True, char_level=False)
tokenizer.fit_on_texts(processed_docs_train )  #leaky
word_seq_train = tokenizer.texts_to_sequences(processed_docs_train)
word_index = tokenizer.word_index
print("dictionary size: ", len(word_index))

#pad sequences
word_seq_train = sequence.pad_sequences(word_seq_train, maxlen=max_seq_len)

print('loading word embeddings...')
import os, re, csv, math, codecs

embeddings_index = {}
f = codecs.open('Embedding/crawl-300d-2M.vec', encoding='utf-8')

for line in tqdm(f):
    values = line.rstrip().rsplit(' ')
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('found %s word vectors' % len(embeddings_index))

#embedding matrix

print('preparing embedding matrix...')
embed_dim = 300
words_not_found = []
nb_words = min(MAX_NB_WORDS, len(word_index)+1)
embedding_matrix = np.zeros((nb_words, embed_dim))

for word, i in word_index.items():
    if i >= nb_words:
        continue
    embedding_vector = embeddings_index.get(word)
    if (embedding_vector is not None) and len(embedding_vector) > 0:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector
    else:
        words_not_found.append(word)
print('number of null word embeddings: %d' % np.sum(np.sum(embedding_matrix, axis=1) == 0))

import tensorflow as tf
from sklearn.model_selection import KFold
kf = KFold(n_splits=10, shuffle=True, random_state=125)
from tensorflow.keras.callbacks import EarlyStopping
#from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping

from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import  precision_score
from sklearn.metrics import  f1_score

#only LSTM
from tensorflow.keras import regularizers

from tensorflow.keras.layers import BatchNormalization
import tensorflow as tf


#max_features =22248
#nb_words=22248
embedding_dim =300
sequence_length = 100

def LSTM_model():
    model =  keras.Sequential()
    #model.add(tf.keras.layers.Embedding(max_features +1, embedding_dim, input_length=sequence_length,\
                                    #embeddings_regularizer = regularizers.l2(0.005))) 
    model.add( keras.layers.Embedding(nb_words,embed_dim,input_length=max_seq_len,weights=[embedding_matrix],trainable=False))
    model.add( keras.layers.Dropout(0.4))

    model.add( keras.layers.LSTM(embedding_dim,dropout=0.2, recurrent_dropout=0.2,return_sequences=True,\
                                                             kernel_regularizer=regularizers.l2(0.005),\
                                                             bias_regularizer=regularizers.l2(0.005)))

    model.add( keras.layers.Flatten())

    model.add( keras.layers.Dense(512, activation='relu',\
                                kernel_regularizer=regularizers.l2(0.001),\
                                bias_regularizer=regularizers.l2(0.001),))
    model.add( keras.layers.Dropout(0.4))

    model.add( keras.layers.Dense(8, activation='relu',\
                                kernel_regularizer=regularizers.l2(0.001),\
                                bias_regularizer=regularizers.l2(0.001),))
    model.add( keras.layers.Dropout(0.4))


    model.add( keras.layers.Dense(1,activation='sigmoid'))
    
    model.compile(loss=tf.keras.losses.BinaryCrossentropy(),optimizer=tf.keras.optimizers.Adam(1e-3),metrics=['acc'])
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

LSTM_model().summary()

from tensorflow.keras.utils import plot_model

#plot_model(LSTM_model(), to_file='LSTMmodel.png', show_shapes=True, show_layer_names=True)

es_callback = EarlyStopping(monitor='val_loss', patience=3)

lstm_run_precision = []
lstm_run_recall = []
lstm_run_f1score = []
lstm_run_accuracy = []

count = 1
num_epochs = 40

for train_index, test_index in kf.split(word_seq_train):
    x_trn, x_tst = word_seq_train[train_index], word_seq_train[test_index]
    y_trn, y_tst = y_train[train_index], y_train[test_index]
    
    x_new_train, x_val, y_new_train, y_val= train_test_split(x_trn, y_trn, test_size=0.11115, random_state=125)
    
    print("\nFold ", count)
    lstm_model=LSTM_model()

    
    
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1)
    
    history =lstm_model.fit( x_new_train, y_new_train, batch_size=256,
          epochs=num_epochs, validation_data=(x_val, y_val), callbacks=[es_callback], shuffle=False)
    
    _, train_acc =lstm_model.evaluate(x_new_train,  y_new_train, verbose=0)
    _, val_acc =  lstm_model.evaluate(x_val, y_val, verbose=0)
    print('Train: %.3f, Test: %.3f' % (train_acc, val_acc))
    
    
     
    #plt.savefig('LSTM with fasttext SE data accuracy graph.png')
    #plt.show()
    
    
    y_pred = lstm_model.predict(x_tst)
    y_pred = (y_pred >= 0.5)
 
    
    from sklearn import metrics
    print(metrics.classification_report(y_tst, y_pred))
    
    lstm_precision = precision_score(y_tst, y_pred, pos_label=1)
    lstm_recall = recall_score(y_tst, y_pred, pos_label=1)
    lstm_f1score = f1_score(y_tst, y_pred, pos_label=1)
    lstm_accuracy = accuracy_score(y_tst, y_pred)

    lstm_run_accuracy.append(lstm_accuracy)
    lstm_run_f1score.append(lstm_f1score)
    lstm_run_precision.append(lstm_precision)
    lstm_run_recall.append(lstm_recall)
    
    count = count+1
    
import tensorflow
from tensorflow.keras.models import Model

from tensorflow.keras.layers import Dense, Input, LSTM,GlobalMaxPool1D
maxlen=max_seq_len
embed_size=300
max_features=nb_words
def Bi_LSTM_base():
    inp = keras.layers.Input(shape=(maxlen,))
    x = tensorflow.keras.layers.Embedding(max_features, embed_size, weights=[embedding_matrix])(inp)
    x = tensorflow.keras.layers.Bidirectional(tensorflow.keras.layers.LSTM(50, return_sequences=True, dropout=0.1, recurrent_dropout=0.1))(x)
    x = tensorflow.keras.layers.GlobalMaxPool1D()(x)
    x = tensorflow.keras.layers.Dense(50, activation="relu")(x)
    x = tensorflow.keras.layers.Dropout(0.1)(x)
    x = tensorflow.keras.layers.Dense(1, activation="sigmoid")(x)
    model = Model(inputs=inp, outputs=x)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
Bi_LSTM_base().summary()
blbase_run_precision = []
blbase_run_recall = []
blbase_run_f1score = []
blbase_run_accuracy = []

count = 1

for train_index, test_index in kf.split(word_seq_train):
    x_trn, x_tst = word_seq_train[train_index], word_seq_train[test_index]
    y_trn, y_tst = y_train[train_index], y_train[test_index]
    
    x_new_train, x_val, y_new_train, y_val= train_test_split(x_trn, y_trn, test_size=0.11115, random_state=125)
    
    print("\nFold ", count)
    bilstmbase_model=Bi_LSTM_base()

    #model_lstm_fasttext=model_with_embedding()
    
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1)
    
    history =bilstmbase_model.fit( x_new_train, y_new_train, batch_size=32,
          epochs=num_epochs, validation_data=(x_val, y_val), callbacks=[es_callback], shuffle=False)
    
    _, train_acc = bilstmbase_model.evaluate(x_new_train,  y_new_train, verbose=0)
    _, val_acc =  bilstmbase_model.evaluate(x_val, y_val, verbose=0)
    print('Train: %.3f, Test: %.3f' % (train_acc, val_acc))
    
    
    y_pred = bilstmbase_model.predict(x_tst)
    y_pred = (y_pred >= 0.5)
 
    
    from sklearn import metrics
    print(metrics.classification_report(y_tst, y_pred))
    
    blbase_precision = precision_score(y_tst, y_pred, pos_label=1)
    blbase_recall = recall_score(y_tst, y_pred, pos_label=1)
    blbase_f1score = f1_score(y_tst, y_pred, pos_label=1)
    blbase_accuracy = accuracy_score(y_tst, y_pred)

    blbase_run_accuracy.append(blbase_accuracy)
    blbase_run_f1score.append(blbase_f1score)
    blbase_run_precision.append(blbase_precision)
    blbase_run_recall.append(blbase_recall)
    
    count = count+1