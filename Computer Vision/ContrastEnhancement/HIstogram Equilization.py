import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/vrind/Downloads/img2.jpg", cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
equ = cv2.equalizeHist(image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([equ], [0], None, [256], [0, 256])

plt.plot(hist, color='b', label='Original')
plt.plot(hist2, color='r', label='Equalized')
plt.xlim([0, 256])
plt.legend()
plt.show()

cv2.imshow('input', mat = image)
cv2.imshow('output', equ)
cv2.waitKey(0)