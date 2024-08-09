import cv2
img = cv2.imread("D:/6thSem/Computer Vision/Images/IMG-20240223-WA0029.jpg",0)

x = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize=5, scale=1)
y = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize=5, scale=1)
absx= cv2.convertScaleAbs(x)
absy = cv2.convertScaleAbs(y)
edge = cv2.addWeighted(absx, 0.5, absy, 0.5,0)
cv2.imshow('edge', edge)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()