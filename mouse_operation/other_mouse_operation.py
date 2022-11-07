import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) == 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
            cv2.imshow('image', img)

img = cv2.imread('C://Users//HP//Desktop//Aksh//Extra//New folder//my_practice_one//imm.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
