#coding:utf-8
import cv2

img = cv2.imread('1.jpg', 0)    #后面参数1表示彩色，0表示黑白。
cv2.imshow('image 1', img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): #wait for 's' key to save and exit
    cv2.imwrite('image.png', img)
    cv2.destroyAllWindows()
