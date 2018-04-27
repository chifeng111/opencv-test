# coding:utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 初始化训练数据
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)

label = np.random.randint(0, 2, (25, 1)).astype(np.float32)

red = trainData[label.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 20, 'r', '^')

blue = trainData[label.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 20, 'b', 's')

# 测试数据
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, label)
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

print 'result:', results
print 'neighbours: ', neighbours
print 'distance: ', dist

plt.show()
