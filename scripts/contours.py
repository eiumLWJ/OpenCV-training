# Boundaries, continuous points
# Contours are not edges mathematically talking, we find contours from edges

import cv2 as cv
import numpy as np


img = cv.imread('Photos/EIUM_Bk.jpeg') # Metodo que obtiene una matriz de la foto

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank', blank)
# Turn into gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
# METHOD 1 : USING BLUR + CANNY (BETTER)
# blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
# # Essentially grab the edges using canny
# canny = cv.Canny(blur, 125, 175)
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# METHOD 2 : USING THRESHOLD
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # Try to binarize the image, below 125 will be considered as 0 and above 255
cv.imshow('Thresh', thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# controus is a python list
# hierarchies are the representations (squares, triangles, etc. used to find the ccontours)
# cv.RETR_TREE all the hierarchical contours
# cv.RETR_EXTERNAL
# cv.CHAIN_APPROX_NONE does nothing, SIMPLE compress the line into two points

print(f'{len(contours)} contour(s) found!')

# Draw the contours
cv.drawContours(blank, contours, -1, (0,255,0),5) #-1 means all of them, 2 is thickness
cv.imshow('Contours Drawn', blank)

# Reduces the contours found by the order of 10

# Another way is using threshold

cv.waitKey(0) #Funcion de teclado que espera una tecla. 0 implica espera infinita
