import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/EIUM_Bk.jpeg') # Obtains a number matrix from the image

cv.imshow('Logo',img)
# Name and variable(matrix) we want to show

# Creation of the mask, which should be the same size than the img
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

masked = cv.bitwise_and(gray,gray,mask=mask)

cv.imshow('Masked', masked)
# Grayscale histogram - peaks represents the intensity of pixels
# Channels for grayscale images can be 0
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256]) # Without mask
gray_hist_mask = cv.calcHist([gray],[0],masked,[256],[0,256]) # With mask

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# plt.figure(1)
# plt.title('Grayscale Histogram_mask')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist_mask)
# plt.xlim([0,256])
# plt.show()

# -----------------------------------------------------------------------------------------------------------
# Colour histogram
colors = ('b','g','r')

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

for i, col in enumerate(colors):
    # hist = cv.calcHist([img], [i], None, [256],[0,256])
    hist = cv.calcHist([img], [i], masked, [256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0) # Keyboard function that waits for a key. 0 implies infinit waiting