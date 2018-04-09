#coding:utf-8

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('3.jpg', 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F, ksize=21)

plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original image')
plt.subplot(122), plt.imshow(laplacian, 'gray'), plt.title('Laplacian')

plt.show()