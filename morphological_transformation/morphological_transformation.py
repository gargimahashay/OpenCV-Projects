import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread('imm1.png')
img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)

dilation = cv.dilate(mask, kernal, iterations=2)
erosion = cv.erode(mask, kernal, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'img', 'th']

images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

