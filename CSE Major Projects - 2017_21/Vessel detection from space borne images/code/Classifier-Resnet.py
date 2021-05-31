#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import gc
import numpy as np 
import pandas as pd
import time


# In[7]:


SHIP_CLASS_NAME = 'ship'
IMAGE_WIDTH     = 768
IMAGE_HEIGHT    = 768
SHAPE           = (IMAGE_WIDTH, IMAGE_HEIGHT)
WORKING_DIR = '/kaggle/working'
INPUT_DIR = '/kaggle/input'
OUTPUT_DIR = '/kaggle/output'

TRAIN_SHIP_SEGMENTATIONS_PATH = os.path.join(INPUT_DIR, 'airbus-ship-detection/train_ship_segmentations_v2.csv')
TRAIN_DATA_PATH = os.path.join(INPUT_DIR, 'airbus-ship-detection/train_v2')
TEST_DATA_PATH = os.path.join(INPUT_DIR, 'airbus-ship-detection/test_v2')


# In[10]:



train = pd.read_csv(TRAIN_SHIP_SEGMENTATIONS_PATH, engine='python')
train.head()


# In[11]:


train['exist_ship'] = train['EncodedPixels'].fillna(0)
train.loc[train['exist_ship'] != 0 , 'exist_ship'] = 1
del train['EncodedPixels']


# In[12]:


print(len(train['ImageId']))
print(train['ImageId'].value_counts().shape[0])

train_gp = train.groupby('ImageId').sum().reset_index()
train_gp.loc[train_gp['exist_ship'] > 0,'exist_ship'] = 1


# In[13]:


print(train_gp['exist_ship'].value_counts())
train_gp = train_gp.sort_values(by='exist_ship')
train_gp = train_gp.drop(train_gp.index[0:100000])


# In[14]:


print(train_gp['exist_ship'].value_counts())
train_sample = train_gp.sample(5000)
print(train_sample['exist_ship'].value_counts())
print (train_sample.shape)


# In[16]:


from PIL import Image

training_img_data = []
target_data = []

data = np.empty((len(train_sample['ImageId']), 256, 256, 3), dtype=np.uint8)
data_target = np.empty((len(train_sample['ImageId'])), dtype=np.uint8)
image_name_list = os.listdir(Train_path)
index = 0

for image_name in image_name_list:
    if image_name in list(train_sample['ImageId']):
        imageA = Image.open(Train_path + image_name).resize((256, 256)).convert('RGB')
        data[index] = imageA
        data_target[index] = train_sample[train_gp['ImageId'].str.contains(image_name)]['exist_ship'].iloc[0]
        index += 1
        
print(data.shape)
print(data_target.shape)


# In[17]:


from sklearn.preprocessing import OneHotEncoder

targets = data_target.reshape(len(data_target), -1)
encoder = OneHotEncoder()
encoder.fit(targets)
targets = encoder.transform(targets).toarray()

print(targets.shape)


# In[18]:


from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(data, targets, test_size=0.2)
x_train.shape, x_val.shape, y_train.shape, y_val.shape


# In[19]:


from keras.preprocessing.image import ImageDataGenerator

img_gen = ImageDataGenerator(rescale=1./255,
                                zca_whitening = False,
                                rotation_range = 90,
                                width_shift_range = 0.2,
                                height_shift_range = 0.2,
                                brightness_range = [0.5, 1.5],
                                shear_range = 0.2,
                                zoom_range = 0.2,
                                horizontal_flip = True,
                                vertical_flip = True)


# In[20]:


from keras.applications.resnet50 import ResNet50 as ResModel

img_width, img_height = 256, 256
model = ResModel(weights='imagenet', include_top=False, input_shape=(img_width, img_height, 3))


# In[21]:


from keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras.models import Sequential, Model 

for layer in model.layers:
    layer.trainable = False

x = model.output
x = Flatten()(x)
x = Dropout(0.8)(x)
x = Dense(1024, activation="relu")(x)
predictions = Dense(2, activation="softmax")(x)
model_final = Model(input = model.input, output = predictions)


# In[23]:


from keras import optimizers

epochs = 30
lrate = 0.0005
decay = lrate/epochs
sgd = optimizers.SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model_final.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
model_final.summary()


# In[24]:


history = model_final.fit_generator(img_gen.flow(x_train, y_train, batch_size=32), 
                                    steps_per_epoch=len(x_train)/32, 
                                    validation_data=(x_val, y_val), 
                                    epochs=epochs)

model_final.save('ShipResnetClassifier.h5')


# In[25]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

acc = history.history['acc']
val_acc = history.history['val_acc']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




