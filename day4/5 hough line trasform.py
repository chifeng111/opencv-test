# coding:utf-8

import cv2
import numpy as np

img = cv2.imread('5.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(img_gray, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=20, maxLineGap=5)
# print lines[0], lines[1]

for x1, y1, x2, y2 in lines[:, 0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('edges', edges)
cv2.imshow('img', img)
cv2.waitKeyEx(0)
cv2.destroyAllWindows()
