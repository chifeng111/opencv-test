# coding:utf-8

import cv2

cap = cv2.VideoCapture('1.avi')

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if ret:
        fgmask = fgbg.apply(frame)

        cv2.imshow('frame', fgmask)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
    else:
        cv2.waitKey(0)
        break

cap.release()
cv2.destroyAllWindows()
