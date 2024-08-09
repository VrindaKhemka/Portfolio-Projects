import cv2
import numpy as np
import math

input=cv2.imread("D:/6thSem/Computer Vision/Images/IMG-20240223-WA0031.jpg",0)
rows=input.shape[0]
columns=input.shape[1]

padded_input=cv2.copyMakeBorder(input,1,1,1,1,cv2.BORDER_REFLECT)
x=padded_input.shape[0]
y=padded_input[1]

lap=np.array([[0,4,0],[4,-16,4],[0,4,0]])
output=np.zeros_like(input)
output1=np.zeros_like(input)

for i in range(rows):
    for j in range(columns):
        sum=0
        sum1=0
        for a in range(3):
            for b in range(3):
                sum+= lap[a,b] * padded_input[a+i,b+j]
        output[i,j]= abs(sum)


f=output- np.min(output)

fs=(255 * (f / np.max(f)))
fs=np.uint8(fs)
output= fs + input

cv2.imshow(winname='input', mat= input)
cv2.imshow(winname='output',mat= output)

key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key== ord('s'):
    cv2.imwrite(filename='negative.png',match=output)
    cv2.destroyAllWindows()