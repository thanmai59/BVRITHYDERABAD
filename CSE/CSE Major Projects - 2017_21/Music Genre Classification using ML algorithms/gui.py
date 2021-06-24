import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import keras
import librosa
import matplotlib.pyplot as plt
#load the trained model to classify the images
from keras.models import load_model
from mgcknn import find_genre

classes = { 
    0:'blues',
    1:'classical',
    2:'country',
    3:'disco',
    4:'hip hop',
    5:'jazz',
    6:'metal',
    7:'pop',
    8:'reggae',
    9:'rock' 
}

top=tk.Tk()
top.geometry('800x600')
top.title('MUSIC GENRE CLASSIFICATION')
top.configure(background='white')
label=Label(top, font=('arial',15,'bold'))
sign_image = Label(top)
options = [
    "k nearest neighbours",
    "random forest",
    "naive bayes",
    "decision tree",
    "support vector machine",
]
clicked = StringVar()
clicked.set( "support vector machine" )
def classify(songname):
    global label_packed
    y, sr = librosa.load(songname, mono=True, duration=5)
    plt.specgram(y, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap='inferno', sides='default', mode='default', scale='dB')
    plt.savefig(f'C:/Users/Raw/Documents/Project/outputs/testImage.png')
    image = Image.open(r'C:/Users/Raw/Documents/Project/outputs/testImage.png') 
    image = image.resize((64,64))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    original, clssifier, predicted = find_genre(songname, clicked.get())
    label.place(relx = 0.470, rely = 0.700)
    label.configure(foreground='#011638', text=classes[predicted])
 
def show_classify_button(file_path):
    classify_b=Button(top,text="Submit",
   command=lambda: classify(file_path),padx=0,pady=0)
    classify_b.configure(background='#364156', foreground='white',
font=('arial',8,'bold'))
    classify_b.place(relx=0.470,rely=0.790)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(r'C:/Users/Raw/Project/outputs/testImage.png')
        uploaded.thumbnail(((top.winfo_width()/2.00),(top.winfo_height()/2.00)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im

        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Select file",command=upload_image,
  padx=0,pady=0 )



upload.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=20)
drop = OptionMenu( top , clicked , *options )
drop.pack(side=BOTTOM)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=RIGHT,expand=True)

heading = Label(top, text="Music genre classification", font=('Times New Roman',20,'bold'))
heading.configure(foreground='black')
heading.pack()
top.mainloop()