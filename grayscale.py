import numpy as np
import cv2

img = cv2.imread('./image_molang.jpg') 

def ImageToGray(image):
    height, width, channel = img.shape 

    img2gray = np.zeros((width, height), np.uint8) 

    for y in  range (0, height):
        for x in range (0, width):
            r = img.item(x,y,2)
            g = img.item(x,y,1)
            b = img.item(x,y,0)

            gray = (int(r) + int(g) + int(b)) / 3.0

            if gray > 255:
                gray = 255

            img2gray.itemset(x,y,gray)
    return img2gray

cv2.imshow('original_img', img)
cv2.imshow('gray_image', ImageToGray(img))

cv2.waitKey(0)
cv2.destroyAllWindows()
