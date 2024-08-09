import cv2

# Read an image from file
image = cv2.imread("D:/6thSem/Computer Vision/Images/gg (12).jpg", cv2.IMREAD_GRAYSCALE)
image2 =cv2.imread("D:/6thSem/Computer Vision/Images/pic2.jpg", cv2.IMREAD_GRAYSCALE)

clahe = cv2.createCLAHE(clipLimit=30, tileGridSize=(70, 70))

# Apply CLAHE to the image
clahe_result1 = clahe.apply(image)
clahe_result2 = clahe.apply(image2)

# Display the original and CLAHE-enhanced images
cv2.imshow("Original Image", image)
cv2.imshow("CLAHE Result 1", clahe_result1)
cv2.imshow("Original Image2", image2)
cv2.imshow("CLAHE Result 2", clahe_result2)
cv2.waitKey(0)
cv2.destroyAllWindows()
