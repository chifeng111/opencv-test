# coding:utf-8

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('3.jpg')

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)  # mask取纯黑白
mask_inv = cv2.bitwise_not(mask)  # mask_inv反转黑白像素

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img1_fg = cv2.bitwise_and(img2, img2, mask=mask)
dst = cv2.add(img1_bg, img1_fg)
img1[0:rows, 0:cols] = dst

plt.subplot(221), plt.imshow(img1_bg), plt.title('img1_bg')
plt.subplot(222), plt.imshow(img1_fg), plt.title('img1_fg')
plt.subplot(223), plt.imshow(dst), plt.title('dst')
plt.subplot(224), plt.imshow(img1), plt.title('img1_new')

plt.show()

# cv2.imshow('image', img1_bg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
