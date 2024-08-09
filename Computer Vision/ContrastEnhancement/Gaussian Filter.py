import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("D:/6thSem/Computer Vision/Images/IMG-20240223-WA0028.jpg", 0)
img1 = cv2.GaussianBlur(img, (11, 11), 2,2)
img2 = abs((2 * img1) - (1 * img))
cv2.imshow('img1', img1)
cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
