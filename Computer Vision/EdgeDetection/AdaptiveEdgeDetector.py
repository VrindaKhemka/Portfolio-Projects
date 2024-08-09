import cv2
import numpy as np

img = cv2.imread("D:/6thSem/Computer Vision/Images/IMG-20240223-WA0032.jpg")
b,g,r = cv2.split(img)


r_gaussian = cv2.GaussianBlur(255-r, (11,11), 1)
cv2.imshow("gaussian", r_gaussian)

def edgeDetection(image):
    size = image.shape
    output = np.zeros_like(image)
    for x in range(size[0] - 9):
        for y in range(size[1] - 9):
            sum = 0
            s = 9
            st = np.std((image[x:x+s, y:y+s]))
            for i in range(3):
                for j in range(3):
                    sum = sum + (image[x+i,y+j] * st)
            output[x,y] = sum
    return output

o = edgeDetection(r_gaussian)
# o = abs(o)
# o = 255-o
cv2.imshow("after", o)

cv2.waitKey(0)
cv2.destroyAllWindows()