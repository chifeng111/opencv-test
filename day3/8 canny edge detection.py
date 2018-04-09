# coding:utf-8

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('3.jpg', 0)

edges = cv2.Canny(img, 50, 100)

plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Orininal image')
plt.subplot(122), plt.imshow(edges, 'gray'), plt.title('edges')

plt.show()
