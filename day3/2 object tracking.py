#coding:utf-8
'''
For HSV, Hue range is [0,179] 色调
Saturation range is [0,255] 饱和度
Value range is [0,255] 明度
'''

import cv2
import numpy as np

# import image
img =cv2.imread('1.jpg')

# convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

# threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# extract the blue object alone
img_blue = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('img', img)
# cv2.imshow('hsv', hsv)
cv2.imshow('mask', mask)
cv2.imshow('img_blue', img_blue)
cv2.waitKey(0)
cv2.destroyAllWindows()