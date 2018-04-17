# coding:utf-8

import cv2
import numpy as np

cap = cv2.VideoCapture('1.avi')

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)  # 创建与frame1同样大小的空白图像
hsv[:, :, 1] = 255  # 将饱和度设置最大

while True:
    ret, frame2 = cap.read()
    if ret:
        next_frame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(prvs, next_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        cv2.imshow('hsv', bgr)
        k = cv2.waitKey(60)
        if k == 27 & 0xff:
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()
