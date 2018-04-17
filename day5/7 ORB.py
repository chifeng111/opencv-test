# coding:utf-8

import cv2

img = cv2.imread('1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find the keypoints with ORB
orb = cv2.ORB()
kp = orb.detect(img, None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw keypoints
img = cv2.drawKeypoints(img, kp, img, (0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
