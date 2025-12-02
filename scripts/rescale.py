import cv2 as cv
img = cv.imread('Photos/EIUM_logo.png')
cv.imshow('Logo',img)

def rescaleFrame(frame,scale=0.75): # Por defecto, 0.75
    width = int(frame.shape[1] * scale) #frame.shape[1] es el ancho
    height = int(frame.shape[0] * scale) #frame.shape[0] es el alto
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Image', resized_image)

# ## RESIZE VIDEOS

# capture = cv.VideoCapture('Videos/Weaves.mp4') # Argumento numerico para la captura de una camara, 0 suele ser la webcam integrada

# # Se usa un bucle para leer de frame en frame

# while True:
#     isTrue, frame = capture.read() # Devuelve el frame y un booleano de lectura exitosa o no
#     frame_resized = rescaleFrame(frame, scale=.2) # Cambiar el tamaño de reescalado
    
#     cv.imshow('Video', frame) # Display de cada frame
#     cv.imshow('Video Resized', frame_resized)

# #     Para salir del bucle, esperamos pulsación de la tecla D
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release() #Liberar dispositivo de captura
# cv.destroyAllWindows() #Cerrar ventanas
