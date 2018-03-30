# coding:utf-8

import cv2
import numpy as np

cap = cv2.VideoCapture('1.avi')

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        frame2hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        img2 = cv2.imread('timg.jpg')

        # define range of blue color in HSV
        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([140, 255, 255])

        # 取出1.jpg中的blue物体
        mask = cv2.inRange(frame2hsv, lower_blue, upper_blue)
        blue = cv2.bitwise_and(frame, frame, mask=mask)

        # 将blue物体合并到timg.jpg中
        mask_inv = cv2.bitwise_not(mask)
        img2_new = cv2.bitwise_and(img2, img2, mask=mask_inv)
        dst = cv2.add(img2_new, blue)


        cv2.imshow('frame', frame)
        cv2.imshow('dst', dst)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
