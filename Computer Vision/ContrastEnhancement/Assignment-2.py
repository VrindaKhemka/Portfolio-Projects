import cv2
import numpy as np

target_image = cv2.imread("D:/6thSem/Computer Vision/Images/HawaMahal.jpg",0)
source_image = cv2.imread("D:/6thSem/Computer Vision/Images/pic2.jpg",0)

mean_t = np.mean(target_image)
r = mean_t + (source_image - mean_t) * (np.std(target_image)/np.std(source_image))
cv2.imshow('image',source_image)
cv2.imshow('target', target_image)
cv2.imshow('trans', r)

cv2.waitKey(0)
cv2.destroyAllWindows()