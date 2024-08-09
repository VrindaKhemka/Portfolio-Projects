import cv2
import numpy as np

x=cv2.imread("D:/6thSem/Computer Vision/Images/HawaMahal.jpg")
h,w,c=x.shape
output_gamma = np.zeros_like(x)
output_gamma_1 = np.zeros_like(x)
output_gamma_2 = np.zeros_like(x)

for i in range(h):
    for j in range(w):
       output_gamma[i,j] = 255 * ((x[i,j]/255) ** 0.5)
       output_gamma_1[i,j] = 255 * ((x[i,j]/255) ** 1)
       output_gamma_2[i,j] = 255 * ((x[i,j]/255) ** 2.6)
       
cv2.imshow(winname='Input', mat=x)
   
cv2.imshow(winname='Gamma 0.5', mat=output_gamma)
cv2.imshow(winname='Gamma 1', mat=output_gamma_1)
cv2.imshow(winname='Gamma 2', mat=output_gamma_2)

cv2.waitKey(0)
