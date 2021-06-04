import tkinter as tk
from keras.preprocessing import image
from PIL import ImageTk, Image
from tkinter import filedialog, Label
from keras.models import load_model
from matplotlib import pyplot as plt
import cv2
import numpy as np
from tkinter.messagebox import *

import torch
from torch import optim,nn
from torch.autograd import Variable
from torch.utils.data import DataLoader,Dataset
from torchvision import models,transforms


model = load_model("/home/lavanya/Downloads/covidDetection.h5")


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    img_path = cv2.imread(filename)
    
    img = image.load_img(filename,target_size=(150,150))

    render = ImageTk.PhotoImage(img)
    img2 = Label(image=render)
    img2.image = render
    img2.place(x=500, y=250)

    images = image.img_to_array(img)
    images= np.expand_dims(images,axis=0)
    prediction = model.predict(images)
    ans = ""
    if prediction == 0:
        ans = "COVID POSITIVE"
    else:
        ans = "COVID NEGATIVE"
    Label(root, text="YOU ARE TESTED " + ans,bg = "white").place(x=500, y=500)


root = tk.Tk()
root.title("COVID - 19 Classification")
root.minsize(750, 1000)
root.resizable(width=True, height = True)
root.configure(bg='black')

heading = Label(root, text="Upload Chest X-ray Image To Get Results", bg = "white").place(x=500, y=150)

button = tk.Button(root, text='SELECT IMAGE', command=UploadAction,bg = "white").place(x=500, y=200)
root.mainloop()
