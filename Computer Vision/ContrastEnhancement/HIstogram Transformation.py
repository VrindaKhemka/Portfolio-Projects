import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("D:/6thSem/Computer Vision/gg (12).jpg")
def img_transformation(source):
    s = (source - np.mean(source)) ** 3
    return s

img2 = img_transformation(img1).astype(np.uint8)
hist = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

plt.plot(hist, color='b', label='Original')
plt.plot(hist2, color='r', label='Equalized')
plt.xlim([0, 256])
plt.legend()
plt.show()

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)