import cv2
import numpy as np 

image = cv2.imread("D:/6thSem/Computer Vision/Images/HawaMahal.jpg")
en_img = image * 2
def find_contrast(img):
    contrast = 0
    for i in range(0,img.shape[0],17):
        for j in range(0,img.shape[1],17):
            mean = np.mean(img[i:i+17 , j:j+17])
            stdd = np.std(img[i:i+17 , j:j+17])
            contrast += stdd/(mean + 0.0001)
    print("Contrast:", contrast/289)

find_contrast(image)
find_contrast(en_img)
