import cv2 as cv
import numpy as np
# Images consists in different channels (RGB), we can split them
img = cv.imread('Photos/EIUM_Bk.jpeg') 

cv.imshow('Logo',img)
b,g,r = cv.split(img)

# Show the actual colour instead grayscale
# Reconstruct the image creating a blank img

blank = np.zeros(img.shape[:2], dtype='uint8')

# Setting other two components to black
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

# Showed as grayscale images (instensity of pixels in that specific colour)
cv.imshow('Blue_Grayscale',b)
cv.imshow('Green_Grayscale',g)
cv.imshow('Red_Grayscale',r)

# Showed as actual colour
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape) # (162, 311, 3)
print(b.shape)   # (162, 311)
print(g.shape)   # (162, 311)
print(r.shape)   # (162, 311)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)



cv.waitKey(0) #Funcion de teclado que espera una tecla. 0 implica espera infinita
