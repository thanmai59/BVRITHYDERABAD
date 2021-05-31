import os
import glob
import random
import tensorflow as tf
from tensorflow.python.data.ops.iterator_ops import Iterator as Iterator
class DataReader:

    def readimage(self,img_path):
        img = tf.io.read_file(str(img_path))
        img = tf.image.decode_jpeg(img,channels=3)
        img = tf.image.resize(img,(480,640))
        img = img / 255.0
        return img

    def readimage1(self,img_path):
        img = tf.io.read_file(img_path)
        img = tf.image.decode_jpeg(img,channels=3)
        img = tf.image.resize(img,(64,64))
        img = img / 255.0
        return img

    def generateTrainTestImages(self,trainImages,testImages):
        trainHazy = tf.data.Dataset.from_tensor_slices([img[0] for img in trainImages]).map(lambda name:self.readimage(name))
        trainNormal = tf.data.Dataset.from_tensor_slices([img[1] for img in trainImages]).map(lambda name:self.readimage(name))
        trainData = tf.data.Dataset.zip((trainHazy,trainNormal)).shuffle(100).repeat().batch(8)
        testHazy = tf.data.Dataset.from_tensor_slices([img[0] for img in testImages]).map(lambda name:self.readimage(name))
        testNormal = tf.data.Dataset.from_tensor_slices([img[1] for img in testImages]).map(lambda name: self.readimage(name))
        testData = tf.data.Dataset.zip((testHazy,testNormal)).shuffle(100).repeat().batch(8)
        itr = Iterator.from_structure(tf.compat.v1.data.get_output_types(trainData),tf.compat.v1.data.get_output_shapes(trainData)) 
        #print("train data", trainData)
        training = itr.make_initializer(trainData)
        testing = itr.make_initializer(testData, name = None)
        print("training", training)
        print("traindata", trainData)
        return training, testing, itr

    def generateExtensionTrainTestImages(self,trainImages,testImages):
        trainHazy = tf.data.Dataset.from_tensor_slices([img[0] for img in trainImages]).map(lambda name: self.readimage1(name))
        trainNormal = tf.data.Dataset.from_tensor_slices([img[1] for img in trainImages]).map(lambda name: self.readimage1(name))
        trainData = tf.data.Dataset.zip((trainHazy,trainNormal)).shuffle(100).repeat().batch(8)
        testHazy = tf.data.Dataset.from_tensor_slices([img[0] for img in testImages]).map(lambda name: self.readimage1(name))
        testNormal = tf.data.Dataset.from_tensor_slices([img[1] for img in testImages]).map(lambda name: self.readimage1(name))
        testData = tf.data.Dataset.zip((testHazy,testNormal)).shuffle(100).repeat().batch(8)
        itr = tf.data.Iterator.from_structure(trainData.output_types,trainData.output_shapes)
        training = itr.make_initializer(trainData)
        #print(training)
        testing = itr.make_initializer(testData)
        #print(testing)
        return training, testing, itr

    def readImages(self,train_images,test_images):
        training_path = glob.glob(train_images + "/*.jpg")
        total_images = len(training_path)
        random.shuffle(training_path)
        trainingKeys = training_path[:int(0.90*total_images)]
        testingKeys = training_path[int(0.90*total_images):]
        imageDict = {}
        for name in trainingKeys:
            imageDict[name] = 'training'
        for name in testingKeys:
            imageDict[name] = 'testing'
        trainImages = []
        testImages = []
        #print(imageDict)
        test_path = glob.glob(train_images + "/*.jpg")
        #print(test_path)
        for name in test_path:
            #print(name)
            imgName = name.split('/')[-1]
            img = os.path.splitext(os.path.basename(name))[0]
            imgpath = train_images + img+".jpg"
            if(imageDict[imgpath] == 'training'):
                trainImages.append([name,imgpath])
            else:
                testImages.append([name,imgpath])
        return trainImages, testImages 
#d = DataReader()     
#trainImages, testImages = d.readImages("/home/goutham/Desktop/Dataset/data/orig_images/","/home/goutham/Desktop/Dataset/data/hazy_images/")
#a,b = d.generateTrainTestImages("/home/goutham/Desktop/Dataset/data/orig_images/","/home/goutham/Desktop/Dataset/data/hazy_images/")   
#a,b,c = d.generateTrainTestImages(trainImages, testImages)    
