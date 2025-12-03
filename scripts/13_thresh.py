import cv2 as cv

# Convert pixels of an image into 0 or 255 depending on the threshold
img = cv.imread('Photos/EIUM_Bk.jpeg')
cv.imshow('Logo',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Thresholding (let the PC to find the optimal threshold value by itself)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3)
cv.imshow('Adative Thresholding', adaptive_thresh)

cv.waitKey(0)