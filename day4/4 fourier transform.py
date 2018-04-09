# coding:utf-8

import cv2
import numpy as np

img = cv2.imread('3.jpg', 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft = np.fft.fftshift(dft)

magnitude_spectrum = 20 * np.log(cv2.magnitude(dft[:, :, 0], dft[:, :, 1]))
cv2.imshow('img', img)
cv2.imshow('dft', magnitude_spectrum)
cv2.waitKey(0)
cv2.destroyAllWindows()
