import numpy as np
import cv2

img = cv2.imread('./image_molang.jpg')

def RandomShift(image, offset=(0.2,0.2), fill=0):
    w, h = image.shape[0:2]
    x, y = offset

    image_copy = image.copy()
    image0 = image_copy[0:int((1-y)*h), 0:int((1-x)*w)]
    
    image[int(y*h):h, int(x*w):w] = image0
    image[0:h, 0:int(x*w)] = fill
    image[0:int(y*h), 0:w] = fill
    
    return image

    

cv2.imshow('image', img)
cv2.imshow('shift_image', RandomShift(img, (0.2, 0.2), 0))

cv2.waitKey(0)
cv2.destroyAllWindows()