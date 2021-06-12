#!/usr/bin/env python3
import numpy as np
import cv2
import math, time, sys
from PIL import Image
from arnold import Arnold
from tkinter import filedialog
import os
import random


def main(argv):
    '''
    path="D:\\P\\Processing\LSB\\Testing_proj\\Test\Dataset\\Real\\"
    files=os.listdir(path)
    image_path =random.choice(files)
    image_path = "D:\\P\\Processing\LSB\\Testing_proj\\Test\Dataset\\Real\\" + image_path'''
    
    
    # Arnold Transform Parameters
    a = 6
    b = 40
    rounds = 33

    # Open the images
    test = np.array(Image.open("choose.png").convert("L"))
                    
    #test = np.array(Image.open(image_path).convert("L"))
    arnold = Arnold(a, b, rounds)
    
    start_time = time.time()
    scrambled = arnold.applyTransformTo(test)
    exec_time = time.time() - start_time
    #print("Transform  execution time: %.6f " % exec_time, "sec")
    im = Image.fromarray(scrambled).convert("L")
    im.save("scrambled_for_secret.png")


def openfn():
    filename = filedialog.askopenfilename(title='Open image to encode')
    return filename


if __name__ == "__main__":
    main(sys.argv[1:])
