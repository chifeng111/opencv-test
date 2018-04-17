# coding:utf-8

import cv2

img = cv2.imread('3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# construct a SIFT object
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img_gray, None)

cv2.drawKeypoints(img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()