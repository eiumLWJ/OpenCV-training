import cv2 as cv
import numpy as np

# Mask is used for focusing on certain parts os an img

img = cv.imread('Photos/EIUM_Bk.jpeg') # Obtains a number matrix from the image
cv.imshow('Logo',img) # Name and variable(matrix) we want to show

# Creation of the mask, which should be the same size than the img
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image',blank)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

# Masked result
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked Image', masked)


cv.waitKey(0) # Keyboard function that waits for a key. 0 implies infinit waiting
