#coding:utf-8
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('img_hsv', img_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(221), plt.imshow(img), plt.title('origin img')
# plt.subplot(222), plt.imshow(img_hsv), plt.title('hsv img')
# plt.subplot(223), plt.imshow(img_gray), plt.title('gray img')
#
# plt.show()
