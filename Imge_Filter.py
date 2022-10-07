import cv2
import numpy as np

path = 'img1.jpg'

def empty(a):
    pass

cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar", 640, 240)
cv2.createTrackbar("Hue_Min", "trackbar", 0, 179, empty)
cv2.createTrackbar("Hue_Max", "trackbar", 176, 179, empty)
cv2.createTrackbar("Sat_Min", "trackbar", 0, 255, empty)
cv2.createTrackbar("Sat_Max", "trackbar", 255, 255, empty)
cv2.createTrackbar("Val_Min", "trackbar", 0, 255, empty)
cv2.createTrackbar("Val_Max", "trackbar", 255, 255, empty)


while True:
    img = cv2.imread(path)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue_Min", "trackbar")
    h_max = cv2.getTrackbarPos("Hue_Max", "trackbar")
    s_min = cv2.getTrackbarPos("Sat_Min", "trackbar")
    s_max = cv2.getTrackbarPos("Sat_Max", "trackbar")
    v_min = cv2.getTrackbarPos("Val_Min", "trackbar")
    v_max = cv2.getTrackbarPos("Val_Max", "trackbar")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(img2, lower, upper)
    imgresult = cv2.bitwise_and(img, img , mask=mask)

    cv2.imshow("img", img)
    cv2.imshow("HSV", img2)
    cv2.imshow("mask", mask)
    cv2.imshow("result", imgresult)

    cv2.waitKey(1)






