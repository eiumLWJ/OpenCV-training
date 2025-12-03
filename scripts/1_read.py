import cv2 as cv

img = cv.imread('Photos/EIUM_Bk.jpeg') # Obtains a number matrix from the image

cv.imshow('Logo',img)
# Name and variable(matrix) we want to show

cv.waitKey(0) # Keyboard function that waits for a key. 0 implies infinit waiting

## READING VIDEOS

capture = cv.VideoCapture('Videos/Weaves.mp4') 
# capture = cv.VideoCapture(0) # Numeric argument refers to connected devices, 0 is the default webcam

# Using a loop for reading frames

while True:
    isTrue, frame = capture.read() # Returns frame and a boolean of the reading status OK/NOK
    cv.imshow('Video', frame) # Display of each frame

    # To get out of the loop, we wait fot D-key
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release() # Free the capture device
cv.destroyAllWindows() # Closing windows
