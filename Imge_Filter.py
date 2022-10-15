import cv2
import numpy as np
import os
import time

start_time = time.time()


path = 'Photos/img44.jpg'
path2 = 'D:\CV_Photos'

def empty(a):
    pass

hue = 0
sat = 0
val = 0
i=0
for hue in range(0, 179,5):
    for sat in range(0, 255,5):
        for val in range(0, 255,5):
            img = cv2.imread(path)
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lower = np.array([hue, sat, val])
            upper = np.array([179, 255, 255])
            mask = cv2.inRange(imgHSV, lower, upper)
            imgResult = cv2.bitwise_and(img, img, mask=mask)
            print(hue, sat, val)
            cv2.imwrite(os.path.join(path2, 'mask_'+str(i)+'.jpg'), mask)
            cv2.imwrite(os.path.join(path2, 'black-white_'+str(i)+'.jpg'), imgResult)
            i=i+1
            cv2.waitKey(0)


print("--- %s seconds ---" % (time.time() - start_time))






