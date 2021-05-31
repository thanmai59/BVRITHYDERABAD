from tkinter import *
import tkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import *
from PIL import Image
import matplotlib.pyplot as plt
from DataReader import DataReader
import cv2
from math import log10, sqrt
import os
from tensorflow.python.framework import ops
main = tkinter.Tk()
main.title("Image Deblurring")
main.geometry("1200x1200")


global dehazed_RGB
global saver
global RGB
global MAX



global filename

def generateCNNModel(RGB):
    cnn1 = Conv2D(3,1,1,padding="same",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(stddev=0.02),
                   kernel_regularizer=tf.keras.regularizers.l2(1e-4))(RGB)#layer 1
    cnn2 = Conv2D(3,3,1,padding="same",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(stddev=0.02),
                   kernel_regularizer=tf.keras.regularizers.l2(1e-4))(cnn1)#layer 2
    encoder1 = tf.concat([cnn1,cnn2],axis=-1) #concatenate layer1 and layer2 to from residual network
    cnn3 = Conv2D(3,5,1,padding="same",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(stddev=0.02),
                   kernel_regularizer=tf.keras.regularizers.l2(1e-4))(encoder1)
    encoder2 = tf.concat([cnn2,cnn3],axis=-1)#concatenate layer2 and layer3 to from residual network
    cnn4 = Conv2D(3,7,1,padding="same",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(stddev=0.02),
                   kernel_regularizer=tf.keras.regularizers.l2(1e-4))(encoder2)
    decoder = tf.concat([cnn1,cnn2,cnn3,cnn4],axis=-1)
    cnn5 = Conv2D(3,3,1,padding="same",activation="relu",use_bias=True,kernel_initializer=tf.initializers.random_normal(stddev=0.02),
                   kernel_regularizer=tf.keras.regularizers.l2(1e-4))(decoder)
    MAX = cnn5 #max layer
    dehaze_cnn = ReLU(max_value=1.0)(tf.math.multiply(MAX,RGB) - MAX + 1.0) #replace pixels intensity
    return dehaze_cnn

def loadModel():
    global dehazed_RGB
    global saver
    global RGB
    global MAX
    dr = DataReader()  #class to read training images
    ops.reset_default_graph() #reset tensorflow graph
    trainImages, testImages = dr.readImages("/home/goutham/Desktop/Datset/data/orig_images/","/home/goutham/Desktop/Datset/data/hazy_images/") #reading normal and haze image to generate tensorflow CNN object
    trainData, testData, itr = dr.generateTrainTestImages(trainImages,testImages)
    print("cnn dehaze ", trainData) 
    next_element = itr.get_next()
    RGB = tf.placeholder(shape=(None,480, 640,3),dtype=tf.float32)
    MAX = tf.placeholder(shape=(None,480, 640,3),dtype=tf.float32)
    dehazed_RGB = generateCNNModel(RGB) #loading and generating model

    trainingLoss = tf.reduce_mean(tf.square(dehazed_RGB-MAX)) #optimizations
    optimizerRate = tf.train.AdamOptimizer(1e-4)
    trainVariables = tf.trainable_variables()
    gradient = optimizerRate.compute_gradients(trainingLoss,trainVariables)
    clippedGradients = [(tf.clip_by_norm(gradients,0.1),var1) for gradients,var1 in gradient]
    optimize = optimizerRate.apply_gradients(gradient)

    saver = tf.train.Saver()
    #pathlabel.config(text='CNN model loaded')
    
def PSNR(original, compressed): 
    mse = np.mean((original - compressed) ** 2) 
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse)) 
    return psnr,mse

def SNR(a, axis=None, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=None, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

#function to allow user to upload images directory
def uploadImage():
    #text.delete('1.0', END)
    global filename
    filename = askopenfilename(initialdir = "TestImages")
    #pathlabel.config(text=filename)
    with tf.Session() as session:
        saver.restore(session,'/home/goutham/Desktop/Deblurr/CNNData/data')
        img = Image.open(filename)
        img = img.resize((640, 480))
        img = np.asarray(img) / 255.0
        img = img.reshape((1,) + img.shape)
        dehazedImage = session.run(dehazed_RGB,feed_dict={RGB:img,MAX:img})
        print(dehazedImage[0])
        orig = cv2.imread(filename)
        orig = cv2.resize(orig,(640, 480),interpolation = cv2.INTER_CUBIC)
        psnr,mse = PSNR(orig,dehazedImage[0].astype('float32') * 255)
        snr = SNR(dehazedImage[0].astype('float32') * 255)
        #text.insert(END,'CNN PSNR : '+str(psnr)+"\n")
        #text.insert(END,'CNN SNR : '+str(snr)+"\n")
        #text.insert(END,'CNN MSE : '+str(mse)+"\n")
        fname = os.path.basename(filename)
        f = open("values.txt", "w")
        f.write(fname+","+str(psnr)+","+str(snr)+","+str(mse))
        f.close()
        figure, axis = plt.subplots(nrows=1, ncols=2,figsize=(10,10))
        axis[0].set_title("Blurr Image")
        axis[1].set_title("Clear Image")
        axis[0].imshow(img[0])
        axis[1].imshow(dehazedImage[0])
        figure.tight_layout()
        plt.show()
    
    

    
def close():
    main.destroy()

font = ('times', 30, 'bold')
f1 = ('ties', 25)
title = Label(main, text='IMAGE DEBLURRING')
title.config(bg='antiquewhite', fg='black')  
title.config(font=font)           
title.config(height=5, width=90)       
title.place(x=50,y=5)
#title.config(anchor = CENTER)
canvas = Canvas(main, width = 500, height = 450)      
canvas.pack()      
img = PhotoImage(file="/home/goutham/Downloads/empire_state.png/")      
canvas.create_image(10,50, anchor=NW, image=img)    
canvas.place(x = 250, y = 400)
t = Text(main, height = 3, width = 95)
t.place(x = 190, y = 200)
t.config(font = f1)
t.config(bg = 'papayawhip')
te = " Deblurring is the process of removing blurring artifacts from images. It is used in medical \n imaging, remote sensing etc."
t.insert(END,te)
font1 = ('times', 20, 'bold')
upload = Button(main, text="Build Model", command=loadModel)
upload.place(x=1100,y=500)
upload.config(font=font1)  

#pathlabel = Label(main)
#pathlabel.config(bg='white', fg='black')  
#pathlabel.config(font=font1)           
#pathlabel.place(x=380,y=100)

dcpButton = Button(main, text="Upload Blur Image", command=uploadImage)
dcpButton.place(x=1100,y=600)
dcpButton.config(font=font1)

exitButton = Button(main, text="Exit", command=close)
exitButton.place(x=1100,y=700)
exitButton.config(font=font1)

#font1 = ('times', 12, 'bold')
#text=Text(main,height=10,width=150)
#scroll=Scrollbar(text)
#text.configure(yscrollcommand=scroll.set)
#text.place(x=10,y=350)
#text.config(font=font1)


main.config(bg='antiquewhite')
main.mainloop()
loadModel()
