import cv2 
import numpy as np
import math 

# img = cv2.imread("D:/6thSem/Computer Vision/Images/WhatsApp Image 2024-02-23 at 15.45.07_0165340d.jpg")
# img = cv2.imread("D:/6thSem/Computer Vision/Images/WhatsApp Image 2024-02-23 at 15.44.20_935fa9ce.jpg") 
img = cv2.imread("D:/6thSem/Computer Vision/Images/IMG-20240223-WA0032.jpg")

imgR = img[:,:,2]
imgR = 255 - imgR

cv2.imshow('red', imgR)
imgR = 255 - imgR
filt=np.array([[1/(math.log2(9**3)),1/(math.log2(9**2)),1/(math.log2(9**3))],
    [1/(math.log2(9**2)),1/(math.log2(9)),1/(math.log2(9**2))],
    [1/(math.log2(9**3)),1/(math.log2(9**2)),1/(math.log2(9**3))]])

padded_imgR=cv2.copyMakeBorder(imgR,1,1,1,1,cv2.BORDER_REFLECT)
x=padded_imgR.shape[0]
y=padded_imgR[1]
rows=imgR.shape[0]
columns=imgR.shape[1]
output=np.zeros_like(imgR)

for i in range(rows):
    for j in range(columns):
        sum=0
        sum1=0
        for a in range(3):
            for b in range(3):
                sum+= filt[a,b] * padded_imgR[a+i,b+j]
        output[i,j]= abs(sum)

cv2.imshow(winname='output',mat= output)
t_lower = 50  
t_upper = 150 

edge = cv2.Canny(output, t_lower, t_upper) 

# cv2.imshow('original', img) 
cv2.imshow('edge', edge) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
