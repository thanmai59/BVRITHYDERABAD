import tkinter as tk
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

#model = load_model("/home/adminpc/Downloads/skinLesionmodel_epo65_acc75.h5")
model = load_model("/home/adminpc/Downloads/skinLesionmodel_epo65_acc75.h5")
#model = torch.load("/home/adminpc/Downloads/slc.h5")

lesionTypeMap = {
    4 : 'Melanocytic nevi',
    5 : 'Melanoma',
    2 : 'Benign keratosis-like lesions ',
    1 : 'Basal cell carcinoma',
    0 : 'Actinic keratoses',
    6 : 'Vascular lesions',
    3 : 'Dermatofibroma'
}
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    img = cv2.imread(filename)
    
    load = Image.open(filename)
    load = load.resize((300, 300), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img2 = Label(image=render)
    img2.image = render
    img2.place(x=100, y=160)

    img.resize(1, 75, 100, 3)
    les_type = np.argmax(model.predict(img), axis=-1)
    print(les_type) 
    Label(root, text=lesionTypeMap[les_type[0]]).place(x=300, y=500)  

root = tk.Tk()
root.title("Skin Lesion Classification")
root.minsize(750, 1000)
root.resizable(width=True, height = True)

heading = Label(root, text="Select image").place(x=100, y=100)
Label(root, text="The lesion type is: ").place(x=100, y = 500)

button = tk.Button(root, text='Upload image', command=UploadAction).place(x=100, y=125)
#blank.insert(0, "1")
#label1 = Label(root, text="Hi").place(x=30, y=30)
root.mainloop()
