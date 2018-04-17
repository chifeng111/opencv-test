# coding:utf-8

import cv2

img = cv2.imread('3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Here I set Hessian Threshold to 400
surf = cv2.xfeatures2d.SURF_create(400)

kp, des = surf.detectAndCompute(img_gray, None)

cv2.drawKeypoints(img, kp, img, (0, 0, 255))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
