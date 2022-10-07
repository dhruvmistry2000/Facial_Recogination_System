import cv2
import numpy as np

path = 'img44.jpg'

def empty(a):
    pass

hue = 0
sat = 0
val = 0
for hue in range(0, 179):
    for sat in range(0, 255):
        for val in range(0, 255):
            img = cv2.imread(path)
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lower = np.array([hue, sat, val])
            upper = np.array([179, 255, 255])
            mask = cv2.inRange(imgHSV, lower, upper)
            imgResult = cv2.bitwise_and(img, img, mask=mask)
            cv2.imshow("Original", img)
            cv2.imshow("HSV", imgHSV)
            cv2.imshow("Mask", mask)
            cv2.imshow("Result", imgResult)
            cv2.waitKey(1)
            print(hue, sat, val)






