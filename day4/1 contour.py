# coding:utf-8
import numpy as np
import cv2

img = cv2.imread('1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
_, contours, hieraarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cnt = contours[0]
M = cv2.moments(cnt)
print M

# show edges
cv2.drawContours(img, contours, -1, color=(0, 255, 0), thickness=2)

# show rotated rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# show straight rectangle
x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# show minimum enclosing circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
cv2.circle(img, (int(x),int(y)), int(radius), (255, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
