# coding:utf-8
## Brute-Force Matching with SIFT Descriptors and Ratio Test

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('8-1.jpg', 0)
img2 = cv2.imread('8-2.jpg', 0)

# initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)