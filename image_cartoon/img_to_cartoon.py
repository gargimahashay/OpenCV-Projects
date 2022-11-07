# imge processing library
import cv2
import numpy as np

# create GUIs
from tkinter.filedialog import *

# ask to open file
photo = askopenfilename()
# for reading the image
img = cv2.imread(photo)
# used to convert color to grey
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# used for processes the edges while removing the noise.
grey = cv2.medianBlur(grey, 5)
edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 230, 230)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("image", img)
cv2.imshow("cartoon", cartoon)

cv2.imwrite("cartoon.jpg", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
