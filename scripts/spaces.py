import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/EIUM_Bk.jpeg') # Metodo que obtiene una matriz de la foto

cv.imshow('Logo',img)
# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

cv.waitKey(0) #Funcion de teclado que espera una tecla. 0 implica espera infinita