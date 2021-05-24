from tkinter import *
from PIL import ImageTk,Image
import scramble as sc
import mpv_main
import inverse_arnold as ia
from tkinter import filedialog
import easygui
import sys
import imageio
import os
import random
import cv2

root=Tk()
root.title('Biometric Steganography')
root.geometry("600x400")
root.config(background="light blue")

def arnold_transform():
    sc.main(sys.argv[1:])
    ar=Toplevel()
    ar.title("Arnold Transformation")
    ar.geometry("600x400")
    ar.config(background="light blue")
    label1 = Label(ar, 
		 text="Scrambled Image",
		 fg = "light green",
		 bg = "dark blue",
		 font = "Helvetica 16 bold italic").pack()
    im = Image.open("scrambled_for_secret.png")
    im = im.resize((250, 250), Image.ANTIALIAS)
    im = ImageTk.PhotoImage(im)
    panel = Label(ar, image=im)
    panel.image = im
    panel.pack()
    b3=Button(ar,text="Proceed to MPV",height = 2, width = 16,command=mpv).pack(pady = 30)

def mpv():
    mpv_main.mpv_encode()
    mpv=Toplevel()
    mpv.title("MPV")
    mpv.geometry("600x400")
    mpv.config(background="light blue")
    label1 = Label(mpv, 
		 text="MPV Image",
		 fg = "light green",
		 bg = "dark blue",
		 font = "Helvetica 16 bold italic").pack()
    im = Image.open("encoded.png")
    im = im.resize((250, 250), Image.ANTIALIAS)
    im = ImageTk.PhotoImage(im)
    panel = Label(mpv, image=im)
    panel.image = im
    panel.pack()
    b3=Button(mpv,text="close", height = 2, width = 16,command=mpv.destroy).pack(pady = 30)

def open():
    en=Toplevel()
    en.title("Encoding")
    en.geometry("600x400")
    en.config(background="light blue")
    image_path = openfn()
    image2 = cv2.imread(image_path)
    cv2.imwrite("choose.png", image2)
    label1 = Label(en, 
		 text="Image to be Encoded ",
		 fg = "light green",
		 bg = "dark blue",
		 font = "Helvetica 16 bold italic").pack()
    im = Image.open("choose.png")
    im = im.resize((250, 250), Image.ANTIALIAS)
    im = ImageTk.PhotoImage(im)
    panel = Label(en, image=im)
    panel.image = im
    panel.pack()
    b2 = Button(en,text="Proceed to arnold",height = 2, width = 16,command=arnold_transform).pack(pady = 30)


    
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def inverse_mpv():
    mpv_main.mpv_decode()
    temp3=Toplevel()
    temp3.title("hidden image")
    temp3.geometry("600x400")
    temp3.config(background="light blue")
    label1 = Label(temp3,
                   text="Scrambled Image ",
                   fg="light green",
                   bg="dark blue",
                   font="Helvetica 16 bold italic").pack()
    img = Image.open("hidden.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(temp3, image=img)
    panel.image = img
    panel.pack()
    #inverse_arnold()
    b9=Button(temp3,text="proceed to inverse arnold",height = 2, width = 20,command=inverse_arnold).pack(pady = 30)
    #print("inverse_mpv_done")
def inverse_arnold():
    ia.main(sys.argv[1:])
    temp4=Toplevel()
    temp4.title("reconstructed image")
    temp4.geometry("600x400")
    temp4.config(background="light blue")
    label1 = Label(temp4,
                   text="Hidden Image ",
                   fg="light green",
                   bg="dark blue",
                   font="Helvetica 16 bold italic").pack()
    img = Image.open("reconstructed.png")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(temp4, image=img)
    panel.image = img
    panel.pack()
    b10=Button(temp4,text="Close",height = 2, width = 16,command=temp4.destroy).pack(pady = 30)
    #print("inverse_arnold done")

def close():
    de=Toplevel()
    de.title("Decoding")
    de.geometry("600x400")
    de.config(background="light blue")
    image_path = openfn()
    image2 = cv2.imread(image_path)
    cv2.imwrite("encoded.png", image2)
    label1 = Label(de, 
		 text="Image to be decoded ",
		 fg = "light green",
		 bg = "dark blue",
		 font = "Helvetica 16 bold italic").pack()
    im = Image.open("encoded.png")
    im = im.resize((250, 250), Image.ANTIALIAS)
    im = ImageTk.PhotoImage(im)
    panel = Label(de, image=im)
    panel.image = im
    panel.pack()
    b8 = Button(de,text="Proceed to inverse MPV",height = 2, width = 18,command=inverse_mpv).pack(pady = 30)

b1=Button(root, text="Encode", height = 2, width = 12, font=("Helvetica", 12, "bold"), bg="purple2", fg="white", command=open).pack(side=TOP,pady=45)
b4=Button(root, text="Decode", height = 2, width = 12, font=("Helvetica", 12, "bold"), bg="purple2", fg="white", command=close).pack(side=TOP,pady=105)
#upload.pack(side=TOP,pady=50)
mainloop()
