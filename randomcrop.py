import numpy as np
import cv2
import random

img = cv2.imread('./image_molang2.jpg')

def RandomCrop(image, size, padding=[[0,0],[0,0],[0,0]], fill=0, padding_mode='constant'):
    image_copy = image.copy()
    w, h = image_copy.shape[0:2]
    w1, h1 = size

    x = random.randint(0, w-1)
    y = random.randint(0, h-1)

    if x >= (w/2):
        if y >= (y/2):
            crop_img = image_copy[y-h1:y, x-w1:x]
        elif y < (y/2):
            crop_img = image_copy[y:y+h1, x-w1:x]
    elif x < (w/2):
        if y >= (y/2):
            crop_img = image_copy[y-h1:y, x:x+w1]
        elif y < (y/2):
            crop_img = image_copy[y:y+h1, x:x+w1]

    print("crop image : ", crop_img)
    if padding == None:
        return crop_img
    else:
        crop_pad_img = np.pad(crop_img, padding, mode=padding_mode)
        return crop_pad_img


cv2.imshow('img', img)
cv2.imshow('crop_image', RandomCrop(img, (400,400), [[5,5],[5,5],[0,0]], 0, 'constant'))

cv2.waitKey(0)
cv2.destroyAllWindows()