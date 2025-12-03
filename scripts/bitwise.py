import cv2 as cv
import numpy as np

# Bitwise operators operates in a binary manner

blank = np.zeros((400,400), dtype='uint8')

corner1= (30,30)
corner2= (370,370)
colour = 255 # white
rectangle = cv.rectangle(blank.copy(), corner1, corner2, colour, -1)
circle = cv.circle(blank.copy(),(200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND --> Intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR --> Non intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR --> Non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT --> Inverse binary values
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)
cv.waitKey(0)
