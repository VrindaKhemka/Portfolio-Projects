import numpy as np
import cv2

orgig=cv2.imread("C:/Users/vrind/Downloads/cameraman.jpg",0)
noise=np.zeros(orgig.shape, np.uint8)
mean = 0
stddev = 1
noise = np.zeros(orgig.shape, np.uint8)
cv2.randn(noise, mean, stddev)

noisy_img = cv2.add(orgig, noise)
output_m=np.zeros_like(orgig)

cv2.imshow(winname='input',mat=orgig)
cv2.imshow(winname='noise',mat=noisy_img)
after_p=cv2.copyMakeBorder(noisy_img,2,2,2,2,cv2.BORDER_REFLECT)

mask=np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])

rows,cols=orgig.shape
r,c=mask.shape
l=[]

for i in range(rows):
    for j in range(cols):
        sum=0
        for a in range(r):
            for b in range(c):
                sum = mask[a,b] * after_p[i+a,j+b]
                l.append(sum)
        l.sort()    
        output_m[i,j]= l[6]
        l.clear()

cv2.imshow(winname='output',mat= output_m)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyAllWindows()
elif key== ord('s'):
    cv2.imwrite(filename='log_trans.png',match=output_m)
    cv2.destroyAllWindows()


