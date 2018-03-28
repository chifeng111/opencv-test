#coding:utf-8
import cv2
import numpy as np

# create a black image
img = np.zeros((512, 512, 3), np.uint8)

# draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# drawing rectangle
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# drawing circle
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# drawing ellipse
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 255, 0), 2)

# drawing polylines
# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# print pts
# pts = pts.reshape((-1,1,2))
# print pts
# cv2.polylines(img, pts, True, (0, 255, 0), 2)

# adding text to image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCv', (10, 450), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('black image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()