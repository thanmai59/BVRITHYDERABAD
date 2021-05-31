import tkinter as tk
from typing import Text
import tensorflow as tf
from keras.preprocessing import image
from PIL import ImageTk, Image
from tkinter import filedialog, Label
from keras.models import load_model
from matplotlib import pyplot as plt
import cv2
import pandas as pd
import numpy as np
from tkinter.ttk import *
from imageio import imread
import matplotlib.pyplot as plt
import matplotlib as mplot
from skimage.segmentation import mark_boundaries
from skimage.measure import label, regionprops
from skimage.morphology import label
from tkinter.messagebox import *

import warnings
warnings.filterwarnings("ignore")

img_width = 768
img_height = 768
model = load_model('ShipResnetClassifier.h5')


def ship_detect(img_path):
  img = tf.keras.preprocessing.image.load_img(img_path, target_size=(256, 256))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images)
  #print(classes)
  if(classes[0][1] > 0.80):
      return "Vessel is detected in the uploaded satellite image.Click on Segment to know where it is located"
  else:
    return "Vessel is not detected in the uploaded satellite image"

def rle_decode(mask_rle,shape):
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths

    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T


def masks_as_image(in_mask_list, all_masks=None):
    if all_masks is None:
        all_masks = np.zeros((768, 768), dtype = np.int16)
    for mask in in_mask_list:
        if isinstance(mask, str):
            all_masks += rle_decode(mask,(768,768))
    return np.expand_dims(all_masks, -1)

def display():
    button1 = tk.Button(root,text = 'Segment', command = mask_generate).place(x = 100,y = 520)
    button1.pack()




def mask_generate():

    ImageId = filename.split("/")[-1]
    #got image id allo fine
    img = imread('test_v2/' + ImageId)
    masks = pd.read_csv("submission.csv")
    rle_mask = masks.query('ImageId=="'+ImageId+'"')['EncodedPixels']
    mask = masks_as_image(rle_mask)
    lbl = label(mask)
    props = regionprops(lbl)
    img1 = img.copy()

    for prop in props:
        print('The coordinates of the ship: ', prop.bbox)
        cv2.rectangle(img1, (prop.bbox[1], prop.bbox[0]), (prop.bbox[4], prop.bbox[3]), (255, 0, 0), 2)
    fig, (ax1,ax2) = plt.subplots(1, 2, figsize = (15, 5))
    ax1.imshow(img)
    ax1.set_title('Uploaded Image')
   # ax2.set_title('Mask')
    ax2.set_title('Image with derived bounding box')
  #  ax2.imshow(mask[...,0], cmap='gray')
    ax2.imshow(img1)
    plt.show()

def UploadAction(root = None):
    global filename
    filename = filedialog.askopenfilename()
    load = Image.open(filename)
    load = load.resize((256,256), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img2 = Label(image=render)
    img2.image = render
    img2.place(x=100, y=160)
    #print(filename)
    img_path = filename.split("/")[-2:]
    img_path = img_path[0] + '/' + img_path[1]
    #print(img_path)
    is_ship_there = ship_detect(img_path)
    Label(root, text=is_ship_there).place(x= 100, y = 420)
    if(is_ship_there == "Vessel is detected in the uploaded satellite image.Click on Segment to know where it is located"):
        display()







root = tk.Tk()
root.title("Vessel Detection from space borne images")
root.minsize(600, 600)
root.resizable(width=True, height = True)
root.config(background = "SlateGray1")
heading = Label(root, text="Upload image to detect vessel",foreground = "maroon1",background = "SlateGray1").place(x=100, y=100)
button = tk.Button(root, text='Upload image', command=UploadAction).place(x=100, y=125)
root.mainloop()
