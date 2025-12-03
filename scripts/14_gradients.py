import cv2 as cv
import numpy as np

# Gradient and edge are mathematically not the same

img = cv.imread('Photos/EIUM_Bk.jpeg') # Obtains a number matrix from the image
cv.imshow('Logo',img)
# Name and variable(matrix) we want to show

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F) # Implies positive and negative slop
lap = np.uint8(np.absolute(lap)) # Turn negative values into positives and transform datatype
cv.imshow('Laplacian', lap)

# Sobel computes gradients in two directions (X, Y) - mostly used in advanced applications
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined sobel', combined_sobel)

# Completely diferent the two gradients methods

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0) # Keyboard function that waits for a key. 0 implies infinit waiting
