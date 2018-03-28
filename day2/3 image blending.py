#coding:utf-8

import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

img3 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
