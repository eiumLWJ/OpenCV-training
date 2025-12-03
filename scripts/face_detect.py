# Using haarcascade
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

import cv2 as cv

img = cv.imread('datasets\FaceDetection\_00394770ca22f389.jpg') 
cv.imshow('Kids',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('scripts\haarcascade_frontalface_default.xml')

# To minimize the noise and avoid detection of non-faces, modify the minNeighbors
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

# Print # os faces
print(f'Number of faces found = {len(faces_rect) }')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0) 
