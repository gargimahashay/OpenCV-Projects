import cv2
import numpy as np


img = cv2.imread('C://Users//HP//Desktop//Aksh//Extra//New folder//my_practice_one//football.jpg')
img2 = cv2.imread('C://Users//HP//Desktop//Aksh//Extra//New folder//my_practice_one//logo.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv2.split(img)


img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))


# ball = img[341:463, 426:532]
# img[66:460, 146:504] = ball


st = cv2.addWeighted(img, 0.8, img2, 0.2, 0)
cv2.imshow('image', st)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
