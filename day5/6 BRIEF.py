# coding:utf-8

import cv2

img = cv2.imread('1.jpg', 0)

# Initiate STAR detector
star = cv2.FeatureDetector_create("STAR")

# Initiate BRIEF extractor
brief = cv2.DescriptorExtractor_create("BRIEF")

# find the keypoints with STAR
kp = star.detect(img, None)

# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)

print brief.getInt('bytes')
print des.shape

img = cv2.drawKeypoints(img, kp, img, (0, 0, 255))
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
