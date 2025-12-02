import cv2 as cv
import numpy as np

# Create a blank pic
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

# # 1· Paint the image a certain colour
# blank[:] = 0,255,0 # : refers to all the pixels, the colour is green (RGB)
# cv.imshow('Green',blank)

# blank[200:300, 300:400] = 0,0,255 # Selecting an area
# cv.imshow('RED Area',blank)

# # 2·Draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=2)
# cv.imshow('BLUE Rectangle',blank)

# # cv.rectangle(blank,(0,0),(250,500),(255,0,0),thickness=cv.FILLED)
# # cv.rectangle(blank,(0,0),(250,500),(255,0,0),thickness=-1) # -1 is the same than cv.FILLED
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=cv.FILLED)
# cv.imshow('BLUE FILLED Rectangle',blank)

# # 3·Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), 40,(0,0,255), thickness=3)
# cv.imshow('RED Circle',blank)

# # 4·Draw a line
# cv.line(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('WHITE line',blank)

# 5·Write text
cv.putText(blank,'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text',blank)

cv.waitKey(0)