import PIL.Image as Image
import numpy as np
import random

def encode(pic_path,text,name,see):
    text = ' '+text
    text = list(text)
    img = Image.open(pic_path)
    width, height = img.size
    pixels = width*height
    if pixels<len(text):
        print("encoding not possible")
    else:
        while True:
            skip = random.randint(3,209)
            if pixels//skip >= len(text):
                break
        edit_image = np.array(img)
        counter = 0
        info = False
        j = 0
        while j < pixels:
            k = j%width
            i = j//height
            if counter >= len(text):
                break
            elif j == 0 and info == False:
                edit_image[i][k][2] = len(text)-1
                edit_image[i][k+1][2] = skip
                info = True
            else:
                edit_image[i][k][2] = ord(text[counter])
                counter += 1
            j+=skip
        new_img = Image.fromarray(edit_image)
        new_img.save(name+".png")
        if see=='y':
            new_img.show()

def decode (pic_path):
    text = ''
    img = Image.open(pic_path)
    img_ar = np.array(img)
    length = img_ar[0][0][2]
    skip = img_ar[0][1][2]
    width, height = img.size
    pixels = width * height
    j = 0
    j += skip
    while j < pixels:
        k = j % width
        i = j // height
        if len(text) > length:
            break
        else:
            text += chr(img_ar[i][k][2])
        j += skip
    print(text)

def main():
    mode = input("Would you like to encode or decode (e/d) : ")
    if mode == 'e':
        im = input('Enter path to image that you want to encode : ')
        name = input("Enter the name of the output file (without extension) : ")
        text = input("Enter the text to be hidden : ")
        see = input('would you like to see the image ? (n/y)')
        encode(im,text,name,see)
    if mode == 'd':
        im = input('Enter path to image that you want to decode : ')
        decode(im)
main()