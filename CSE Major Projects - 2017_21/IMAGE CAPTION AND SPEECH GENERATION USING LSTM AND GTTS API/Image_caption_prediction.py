from pickle import load
from numpy import argmax
from keras.preprocessing.sequence import pad_sequences
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from keras.models import load_model

from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk

from gtts import gTTS

root = Tk()
root.title("Image Caption and Speech Generator")
root.geometry("700x700")
root.configure(bg='azure')

global res

l = Label(root)

def showimage():
	fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG file", "*.png"), ("All Files", "*.*")))
	showimage.img_path = fln
	img = Image.open(fln)
	img.thumbnail((550,550))
	img = ImageTk.PhotoImage(img)
	lbl.configure(image=img, pady=35, bd="25", bg = "azure",relief="solid")
	lbl.image = img
	photo = extract_features(showimage.img_path)
	description = generate_desc(model, tokenizer, photo, max_length)
	sublist = ["startseq", "endseq"]
	for sub in sublist:
		description = description.replace(sub,' ')
	res = " ".join(description.split())
	l.config(text=res,font=("Georgia", 14, "bold"),padx=10,pady=25,bg="azure")
	showimage.f = res
	l.pack()


def play():
    tts = gTTS(text=showimage.f, lang='en')
    tts.save('myfile.mp3')
    os.system("mpg321 myfile.mp3")


frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)
frm.config(bg="azure")


lbl = Label(root)
lbl.pack()



def extract_features(filename):

	model = VGG16()
	model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
	image = load_img(filename, target_size=(224, 224))
	image = img_to_array(image)
	image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
	image = preprocess_input(image)
	feature = model.predict(image, verbose=0)
	return feature


def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None


def generate_desc(model, tokenizer, photo, max_length):
	in_text = 'startseq'
	for i in range(max_length):
		sequence = tokenizer.texts_to_sequences([in_text])[0]
		sequence = pad_sequences([sequence], maxlen=max_length)
		yhat = model.predict([photo,sequence], verbose=0)
		yhat = argmax(yhat)
		word = word_for_id(yhat, tokenizer)
		if word is None:
			break
		in_text += ' ' + word
		if word == 'endseq':
			break
	return in_text


tokenizer = load(open('/home/user/Downloads/tokenizer.pkl', 'rb'))

max_length = 34

model = load_model('/home/user/Downloads/model_6.h5')

btn = Button(frm, text="Browse Image", font="bold", command=showimage, bg="white")
btn.pack(side=tk.LEFT)

btn3 = Button(frm, text="play", font="bold", bg="white", command=play)
btn3.pack(side=tk.LEFT, padx=20)

btn2 = Button(frm, text="Exit", font="bold", bg="white", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)

root.mainloop()
