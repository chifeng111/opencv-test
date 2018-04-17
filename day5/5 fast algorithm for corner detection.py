#coding:utf-8

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# initiate FAST object with default values
fast = cv2.FastFeatureDetector()

kp = fast.detect(img_gray, None)
img2 = cv2.drawKeypoints(img, kp, None, (0, 0, 255))

# disable nonmaxSuppression
fast.setBool('nonmaxSuppression', 0)
kp2 = fast.detect(img_gray, None)

img3 = cv2.drawKeypoints(img, kp2, None, (0, 0, 255))

plt.subplot(121), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)), plt.title('FAST with nonmaxSuppression')

plt.subplot(122), plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)), plt.title('FAST without nonmaxSuppression')

plt.show()