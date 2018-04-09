# coding:utf-8
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('3.jpg', 0)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.subplot(222), plt.imshow(th1, 'gray'), plt.title('Global Thresholding')
plt.subplot(223), plt.imshow(th2, 'gray'), plt.title('Adaptive Mean Thresholding')
plt.subplot(224), plt.imshow(th3, 'gray'), plt.title('Adaptive Gaussian Thresholding')

plt.show()
