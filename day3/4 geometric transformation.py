# coding:utf-8

import cv2
import numpy as np

img = cv2.imread('1.jpg')

# scaling
# height, width = img.shape[:2]
# res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('original', img)
# cv2.imshow('res', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# rotation
height, width = img.shape[0:2]
M = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)# 获取旋转矩阵
dst = cv2.warpAffine(img, M, (width, height))
cv2.imshow('res', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
