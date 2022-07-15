import numpy as np
import cv2

img = cv2.imread('./cream_molang.jpg')

def Blur(image, size, mode='Average'):
    copy_img = img.copy()
    numRows, numCols = copy_img.shape[0:2]

    r_img = copy_img[:, :, 0]
    g_img = copy_img[:, :, 1]
    b_img = copy_img[:, :, 2]

    r = copy_img.copy()[:,:,0]
    g = copy_img.copy()[:,:,1]
    b = copy_img.copy()[:,:,2]

    halfBoxSize = int(size / 2)
    startRow = halfBoxSize
    startCol = halfBoxSize

    if mode == 'Average':
        for row in range(startRow, numRows-halfBoxSize):
            for col in range(startCol, numCols-halfBoxSize):
                localPixels_r = r_img[row - halfBoxSize:row + halfBoxSize + 1, col - halfBoxSize:col + halfBoxSize + 1]
                localPixels_g = g_img[row - halfBoxSize:row + halfBoxSize + 1, col - halfBoxSize:col + halfBoxSize + 1]
                localPixels_b = b_img[row - halfBoxSize:row + halfBoxSize + 1, col - halfBoxSize:col + halfBoxSize + 1]

                blurredValue_r = np.mean(localPixels_r)
                blurredValue_g = np.mean(localPixels_g)
                blurredValue_b = np.mean(localPixels_b)

                r[row, col] = blurredValue_r
                g[row, col] = blurredValue_g
                b[row, col] = blurredValue_b

        blur_img = np.dstack((r, g, b))
        blur_img = blur_img.astype(np.uint8)
        return blur_img

    elif mode == 'Median':
        for row in range(startRow, numRows-halfBoxSize):
            for col in range(startCol, numCols-halfBoxSize):
                localPixels_r = r_img[row - halfBoxSize:row + halfBoxSize + 1, col - halfBoxSize:col + halfBoxSize + 1]
                localPixels_g = g_img[row - halfBoxSize:row + halfBoxSize + 1, col - halfBoxSize:col + halfBoxSize + 1]
                localPixels_b = b_img[row - halfBoxSize:row + halfBoxSize + 1, col - halfBoxSize:col + halfBoxSize + 1]

                blurredValue_r = np.mean(localPixels_r)
                blurredValue_g = np.mean(localPixels_g)
                blurredValue_b = np.mean(localPixels_b)

                r[row, col] = blurredValue_r
                g[row, col] = blurredValue_g
                b[row, col] = blurredValue_b

        blur_img = np.dstack((r, g, b))
        blur_img = np.core.records.fromarray(blur_img.astype(np.uint8))
        return blur_img



cv2.imshow('image', img)
cv2.imshow('blur_image', Blur(img, 8, 'Average'))

cv2.waitKey(0)
cv2.destroyAllWindows()