import cv2
import numpy as np

image = cv2.imread("D:/6thSem/Computer Vision/Images/HawaMahal.jpg", 0)

# Adjust contrast (simple version)
C = np.mean(image)  # Global mean
enhanced_image = C + (image - C) * 1.2

# Clip pixel values to ensure they remain within the valid range [0, 255]
enhanced_image = np.clip(enhanced_image, 0, 255).astype(np.uint8)

cv2.imshow("Original Image", image)
cv2.imshow("Contrast Enhanced Image", enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
