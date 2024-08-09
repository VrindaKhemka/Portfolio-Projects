from skimage.exposure import cumulative_distribution
import matplotlib.pylab as plt
import numpy as np

def cdf(im):
    c, b = cumulative_distribution(im) 
    c = np.insert(c, 0, [0]*b[0])
    c = np.append(c, [1]*(255-b[-1]))
    return c

def hist_matching(c, x, im):
    pixels = np.arange(256)
    new_pixels = np.interp(c, x, pixels) 
    im = (np.reshape(new_pixels[im.ravel()], im.shape)).astype(np.uint8)
    return im

im = plt.imread("D:/6thSem/Computer Vision/Images/pic2.jpg")
template = plt.imread("D:/6thSem/Computer Vision/Images/HawaMahal.jpg")

plt.figure()
plt.imshow(im, cmap='gray')
plt.title('Input Image')
 
c = cdf(im)
x = cdf(template)

im = hist_matching(c, x, im)
plt.figure()
plt.imshow(im, cmap='gray')
plt.title('Matched Image')

plt.figure()
plt.imshow(template, cmap='gray')
plt.title('Template Image')

plt.show()



