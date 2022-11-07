import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# for showing all the events in my system

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green)+ ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (0, 255, 0), 2)
        cv2.imshow('image', img)

img = cv2.imread('C://Users//HP//Desktop//Aksh//Extra//New folder//my_practice_one//imm.jpg')
# img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)


cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()