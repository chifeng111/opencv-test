#coding:utf-8

import cv2
import numpy as np

img = cv2.imread('5.jpg')
img = cv2.medianBlur(img, 5) #模糊滤波，去噪
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1, 120,
                           param1=100, param2=30, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))

for x, y, radiu in circles[0,:]:
    cv2.circle(img, (x,y), radiu, (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()