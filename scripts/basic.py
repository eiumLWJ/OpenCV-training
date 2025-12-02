import cv2 as cv

img = cv.imread('Photos/EIUM_Bk.jpeg') 

cv.imshow('Logo',img)

# # Converting to grayScale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# Blur (remove noise)
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) #ksize is kernel size
cv.imshow('Blur',blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175) # To reduce edges we can use blur img instead of original img
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny,(3,3), iterations=3)
cv.imshow('Dilated', dilated)

# Eroded - going back to pre-dilating (not the same)
eroded = cv.erode(dilated,(3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize ignoring the aspect ratio
resized = cv.resize(img,(500,500), interpolation = cv.INTER_AREA) #dsize is destination size
# For reducing, INTER_AREA
# For augmenting, INTER_LINEAR or INTER_CUBIC (the slowest, but more quality)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Crepped', cropped)
cv.waitKey(0) #Funcion de teclado que espera una tecla. 0 implica espera infinita
