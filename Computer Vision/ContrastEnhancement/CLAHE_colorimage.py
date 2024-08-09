import cv2
import numpy as np
from matplotlib import pyplot as plt

def showimage(myimage, figsize=[10,10]):
    if myimage.ndim > 2:
        myimage = myimage[:,:,::-1]  # Convert BGR to RGB
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(myimage, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # Hide tick values on X and Y axis
    plt.show()

# Read the color image
colorimage = cv2.imread("D:/6thSem/Computer Vision/Images/pic2.jpg")

# Apply CLAHE separately to each channel
clahe_model = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
colorimage_b = clahe_model.apply(colorimage[:,:,0])
colorimage_g = clahe_model.apply(colorimage[:,:,1])
colorimage_r = clahe_model.apply(colorimage[:,:,2])

# Stack the processed channels to form the resultant image
colorimage_clahe = np.stack((colorimage_b, colorimage_g, colorimage_r), axis=2)

# Plot histograms for each channel
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr, _ = np.histogram(colorimage_clahe[:,:,i], 256, [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
for i, col in enumerate(color):
    histr, _ = np.histogram(colorimage[:,:,i], 256, [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
# Display the original and CLAHE adjusted images
showimage(colorimage)
showimage(colorimage_clahe)
