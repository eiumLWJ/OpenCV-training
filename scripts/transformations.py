import cv2 as cv
import numpy as np

img = cv.imread('Photos/EIUM_Bk.jpeg') 

cv.imshow('Logo',img)

# Translation
# Shift in X and Y axis
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # getting dimensions of the image
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img,100,100) # To the Right and Down 100 pixels
cv.imshow('Translated', translated)

# Rotation by some angle
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2] # :2 first two values

    if rotPoint is None: # Rotate by center
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated_rotated', rotated_rotated)
# Introduce black triangles, because once it is rotated, there is no more pixels outside the frame

# Flipping
# 0 - vertically
# 1 - horizontally
# -1 - both
flip = cv.flip(img, 0)
cv.imshow('Flipped',flip)
cv.waitKey(0) 


#Cropping
