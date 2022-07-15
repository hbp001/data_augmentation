import numpy as np
import cv2

img = cv2.imread('./image_molang1.jpg')


def HorizontalFlip(image):
    ver_img = np.fliplr(img)

    return ver_img

cv2.imshow('img', img)
cv2.imshow('horizontal_image', HorizontalFlip(img))

cv2.waitKey(0)
cv2.destroyAllWindows()