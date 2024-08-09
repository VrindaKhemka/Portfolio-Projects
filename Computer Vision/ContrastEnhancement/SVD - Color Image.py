import numpy as np
import cv2

# Ensure correct paths and image loading
img = cv2.imread("D:/6thSem/Computer Vision/Images/HawaMahal.jpg")
target_img = cv2.imread("D:/6thSem/Computer Vision/Images/pic2.jpg")
cv2.imshow("image", img)
cv2.imshow("target", target_img)
# Convert to Lab color space
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
lab_target = cv2.cvtColor(target_img, cv2.COLOR_BGR2Lab)

# Split Lab images
L, a, b = cv2.split(lab_img)
L_target, _, _ = cv2.split(lab_target)

# Compute mean values
mean_target = np.mean(L_target)
mean_original = np.mean(L)

L = np.float32(L) / 255.0
L_target = np.float32(L_target) / 255.0

# Ensure both L and L_target are resized to the same size
L = cv2.resize(L, (512, 512))
L_target = cv2.resize(L_target, (512, 512))

# Perform SVD
U, S, Vt = np.linalg.svd(L)

# Adjust contrast enhancement factor (experiment with different values)
contrast_factor = np.std(L_target) / np.std(L)

# Modify singular values with caution to avoid clipping
S_contrast = S * contrast_factor

# Reconstruct and clip (ensure data types are compatible)
Lk = np.dot(U, np.dot(np.diag(S_contrast), Vt))
Lk = np.clip(Lk, 0, 1)


L_contrast = np.uint8(Lk * 255)
print((L_contrast.shape, np.uint8(a).shape, np.uint8(b).shape))

a = cv2.resize(a, (512, 512))
b = cv2.resize(b, (512, 512))
# Merge channels with consistent data types
lab_output = cv2.merge((L_contrast, np.uint8(a), np.uint8(b)))

# Convert back to RGB and display
output = cv2.cvtColor(lab_output, cv2.COLOR_Lab2BGR)
cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
