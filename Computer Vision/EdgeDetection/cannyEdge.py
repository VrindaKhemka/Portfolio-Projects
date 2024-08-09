import cv2 

# img = cv2.imread("D:/6thSem/Computer Vision/Images/WhatsApp Image 2024-02-23 at 15.45.07_0165340d.jpg")
# img = cv2.imread("D:/6thSem/Computer Vision/Images/WhatsApp Image 2024-02-23 at 15.44.20_935fa9ce.jpg") 
img = cv2.imread("D:/6thSem/Computer Vision/Images/IMG-20240223-WA0032.jpg")


t_lower = 120  
t_upper = 150 

edge = cv2.Canny(img, t_lower, t_upper) 
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sub = edge + img1
cv2.imshow('sub', sub)
cv2.imshow('original', img) 
cv2.imshow('edge', edge) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
