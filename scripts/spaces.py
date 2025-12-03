import cv2 as cv
import matplotlib.pyplot as plt # MATLAB-like figure GUI

img = cv.imread('Photos/EIUM_Bk.jpeg') 
cv.imshow('Logo', img)

# # OpenCV use BGR instead of RGB as most libraries does
# plt.imshow(img)
# plt.show()

# cv.imshow('Logo',img)
# # BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# # BGR to RGB
# rgb = cv.cvtColor(img,cv.COLOR_RGB2BGR)
# cv.imshow ('RGB',rgb)

# plt.imshow(rgb)
# plt.show()

# For any other conversion, we need to pass throught BGR, we cannot turn Gray scale to HSV
# # HSV to BGR
# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow ('HSV --> BGR',hsv_bgr)

# Lab to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow ('Lab --> BGR',lab_bgr)

cv.waitKey(0) #Funcion de teclado que espera una tecla. 0 implica espera infinita 