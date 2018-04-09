# coding:utf-8

import cv2
import matplotlib.pyplot as plt

original = cv2.imread('3.jpg')
original_hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

# 选取原图中的草坪部分，作为目标
target = original[300:, 500:]
target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# 计算直方图
target_hist = cv2.calcHist([target_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# 归一化并反向投影
cv2.normalize(target_hist, target_hist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([original_hsv], [0, 1], target_hist, [0, 180, 0, 256], 1)

# 对反向投影进行卷积操作，很重要
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(dst, -1, disc, dst)

# 调阈值和位运算
ret, thresh = cv2.threshold(dst, 50, 255, 0)
# thresh = cv2.merge((thresh, thresh, thresh))
res = cv2.bitwise_and(original, original, mask=thresh)

plt.subplot(221), plt.imshow(original), plt.title('original_img')
plt.subplot(222), plt.imshow(target), plt.title('target_img')
plt.subplot(223), plt.imshow(thresh, 'gray'), plt.title('mask')
plt.subplot(224), plt.imshow(res), plt.title('res')
plt.show()

# cv2.imshow('thresh', thresh)
# cv2.imshow('res', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
