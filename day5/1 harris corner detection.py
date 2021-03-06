# coding:utf-8

import cv2
import numpy as np

img = cv2.imread('1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_float = np.float32(img_gray)
dst = cv2.cornerHarris(img_float, 2, 3, 0.04)

print dst

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
