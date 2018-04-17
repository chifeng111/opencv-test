# coding:utf-8
## Brute-Force Matching with ORB Descriptors

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('8-1.jpg', 0)
img2 = cv2.imread('8-2.jpg', 0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# create BFMatcher object and match descriptors
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# sort matches in the roder of their distance
matches = sorted(matches, key=lambda x: x.distance)

# draw first 10 matches
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

plt.imshow(img3)
plt.show()
