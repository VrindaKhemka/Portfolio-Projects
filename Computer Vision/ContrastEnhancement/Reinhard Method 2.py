import cv2
import numpy as np

def reinhard_color_normalization(source, target, clip_limit=2.0):
    # Convert source and target images to LAB color space
    source_lab = cv2.cvtColor(source, cv2.COLOR_BGR2LAB)
    target_lab = cv2.cvtColor(target, cv2.COLOR_BGR2LAB)

    # Split LAB channels
    source_l, source_a, source_b = cv2.split(source_lab)
    target_l, target_a, target_b = cv2.split(target_lab)

    
    # Apply Reinhard formula
    source_l_eq = np.mean(target_l) + (source_l - np.mean(source_l)) * (np.std(target_l) / np.std(source_l))
    source_a_eq = np.mean(target_a) + (source_a - np.mean(source_a)) * (np.std(target_a) / np.std(source_a))
    source_b_eq = np.mean(target_b) + (source_b - np.mean(source_b)) * (np.std(target_b) / np.std(source_b))

    # Merge LAB channels back
    source_lab_eq = cv2.merge([source_l_eq, source_a_eq, source_b_eq])

    # Convert back to BGR color space
    source_normalized = cv2.cvtColor(source_lab_eq.astype(np.uint8), cv2.COLOR_LAB2BGR)

    return source_normalized

target_image = cv2.imread("D:/6thSem/Computer Vision/Images/HawaMahal.jpg")
source_image = cv2.imread("D:/6thSem/Computer Vision/Images/pic2.jpg")

# Perform Reinhard color normalization
normalized_image = reinhard_color_normalization(source_image, target_image)

# Display the source, target, and normalized images
cv2.imshow("Source Image", source_image)
cv2.imshow("Target Image", target_image)
cv2.imshow("Reinhard Normalized Image", normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
