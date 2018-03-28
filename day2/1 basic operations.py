# coding:utf-8
import cv2
import numpy as np

img = cv2.imread('1.jpg', 1)

# accessing px values
px = img[100, 100]
print px

# accessing and modifying red value
print img.item(100, 100, 2)
img.itemset((100, 100, 2), 100)
print img.item(100, 100, 2)

# accessing image properties
print img.shape
print img.size
print img.dtype

# splitting and merging image channels
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# or
b = img[:, :, 0]

# remove green pixels
img[:, :, 1] = 0
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

