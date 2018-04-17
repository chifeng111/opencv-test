# coding:utf-8

import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture('1.avi')

# take first frame and setup initial location for window
ret, frame = cap.read()
x, y, w, h = 116, 350, 130, 130
track_window = (x, y, w, h)

# set up the ROI for tracking
roi = frame[y:y + h, x:x + w]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(roi_hsv, np.array((0, 60, 32)), np.array((180, 255, 255)))
roi_hist = cv2.calcHist([roi_hsv], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
# plt.imshow(mask, 'gray'), plt.show()

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # apply meanshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # draw track_window on image
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame, [pts], True, (0, 0, 255), 2)
        cv2.imshow('img2', img2)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
