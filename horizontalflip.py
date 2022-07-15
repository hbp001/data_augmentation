import numpy as np
import cv2

img = cv2.imread('./image_molang1.jpg')

print("img_array : ", img)
# def HorizontalFlip(image):

ho_img = np.flipud(img)

cv2.imshow('img', img)
cv2.imshow('horizontal_image', ho_img)

cv2.waitKey(0)
cv2.destroyAllWindows()