import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load a color image
# img = cv2.imread("C:/Users/vrind/Downloads/cameraman.jpg")
img = cv2.imread("D:/6thSem/Computer Vision/Images/gg (12).jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
A = np.float32(img) / 255.0  


U, S, Vt = np.linalg.svd(A)

contrast_factor = 2.6
S_contrast = S * contrast_factor

Ak = np.dot(U, np.dot(np.diag(S_contrast), Vt))

cv2.imshow('output', Ak)
cv2.waitKey(0)