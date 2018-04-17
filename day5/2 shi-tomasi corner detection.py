#coding:utf-8

import cv2
import numpy as np

img = cv2.imread('1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(img_gray, 25, 0.01, 10)
corners = np.int0(corners)

for x, y in corners[:, 0]:
    cv2.circle(img, (x,y), 3, (0, 0, 255), -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()