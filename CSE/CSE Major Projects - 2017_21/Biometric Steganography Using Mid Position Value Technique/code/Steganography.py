import numpy as np
from tkinter import filedialog
import cv2
import random
from PIL import Image
from matplotlib import pyplot as plt
import os
import random

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def show_image(image1, image2):
    plt.figure('Picture')
    plt.subplot(121)  
    plt.imshow(image1[:, :, ::-1])
    plt.subplot(122)
    plt.imshow(image2[:, :, ::-1])
    plt.show()  
    plt.axis('off')



def check_image_extension(image_name):
    if image_name.split(".")[1] != "PNG" and image_name.split(".")[1] != "png":
        raise Exception('Image extension is incorrect, should be "PNG" or "png"!')



def encode_image():
    image1_name = "scrambled_for_secret.png"
    check_image_extension(image1_name)

    path="C:\\Users\\nissa\\OneDrive\\Desktop\\Major\\Final_MPV\\Real\\"
    files=os.listdir(path)
    image_path =random.choice(files)
    image2_name = "C:\\Users\\nissa\\OneDrive\\Desktop\\Major\\Final_MPV\\Real\\" + image_path

    #image2_name = openfn()


    check_image_extension(image2_name)


    image1 = cv2.imread(image2_name)
    image2 = cv2.imread(image1_name)
    cv2.imwrite("cover.png", image2)


    if image2.shape[0] > image1.shape[0] and image2.shape[1] > image1.shape[1]:
        raise Exception('Image 2 should be smaller or equal to image1!')

    for i in range(image2.shape[0]):
        for j in range(image2.shape[1]):
            for k in range(3):
                binary_image1 = format(image1[i][j][k], '08b')
                binary_image2 = format(image2[i][j][k], '08b')

                new_pixel_binary = binary_image1[:4] + binary_image2[:4]  # concatenation bits
                #new_pixel_binary = binary_image1[2:6] + binary_image2[2:6]
                
                image1[i][j][k] = int(new_pixel_binary, 2)  # modify the image1's pixels to int

    new_image_name = "encoded.png"

    check_image_extension(new_image_name)

    cv2.imwrite(new_image_name, image1)


def decode_image():
    image_name = "encoded.png"
    check_image_extension(image_name)

    merge_image = cv2.imread(image_name)

    original_image_name = "datasetpic.png"
    check_image_extension(original_image_name)

    decrypted_image_name = "hidden.png"
    check_image_extension(decrypted_image_name)

    width = merge_image.shape[0]
    height = merge_image.shape[1]

    image1 = np.zeros((width, height, 3), np.uint8)
    image2 = np.zeros((width, height, 3), np.uint8)

    for i in range(width):
        for j in range(height):
            for k in range(3):
                binary_merge_image = format(merge_image[i][j][k], '08b')
                binary_image1 = binary_merge_image[:4] + chr(random.randint(0, 1) + 48) * 4
                binary_image2 = binary_merge_image[4:] + chr(random.randint(0, 1) + 48) * 4

               
                image1[i][j][k] = int(binary_image1, 2)
                image2[i][j][k] = int(binary_image2, 2)

   
    cv2.imwrite(original_image_name, image1)
    cv2.imwrite(decrypted_image_name, image2)

    
    #show_image(image1, image2)


def convert_text_2_binary(text):
    binary = [format(ord(value), '08b') for value in text]
    return binary


def modify_pixels(pixels, text):
    binary_list = convert_text_2_binary(text)
    length_text = len(binary_list)
    image_data = iter(pixels)

    for i in range(length_text):
        pixels = [j for j in image_data.__next__()[:3] + image_data.__next__()[:3] + image_data.__next__()[:3]]


        for j in range(0, 8):
            if binary_list[i][j] == '0' and pixels[j] % 2 != 0:
                pixels[j] -= 1

            elif binary_list[i][j] == '1' and pixels[j] % 2 == 0:
                # check if the pixel is not 0 to prevent exceed from the range
                if pixels[j] != 0:
                    pixels[j] -= 1
                else:
                    pixels[j] += 1

        if i == length_text - 1:
            if pixels[-1] % 2 == 0:
                if pixels[-1] != 0:
                    pixels[-1] -= 1
                else:
                    pixels[-1] += 1

        else:
            if pixels[-1] % 2 != 0:
                pixels[-1] -= 1

        pixels = tuple(pixels)

        yield pixels[0:3]
        yield pixels[3:6]
        yield pixels[6:9]


def new_image_pixels(new_image, text):
    width = new_image.size[0] 
    (x, y) = (0, 0) 


    for pixel in modify_pixels(new_image.getdata(), text):
        new_image.putpixel((x, y), pixel)
        if x == width - 1: 
            x = 0
            y += 1
        else:
            x += 1
