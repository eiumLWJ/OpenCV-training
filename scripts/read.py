import cv2 as cv

img = cv.imread('Photos/EIUM_Bk.jpeg') # Metodo que obtiene una matriz de la foto

cv.imshow('Logo',img)
# Logo es el nombre de la ventana y img la variable donde hemos guardado la foto

cv.waitKey(0) #Funcion de teclado que espera una tecla. 0 implica espera infinita

## READING VIDEOS

capture = cv.VideoCapture('Videos/Weaves.mp4') # Argumento numerico para la captura de una camara, 0 suele ser la webcam integrada

# Se usa un bucle para leer de frame en frame

while True:
    isTrue, frame = capture.read() # Devuelve el frame y un booleano de lectura exitosa o no
    cv.imshow('Video', frame) # Display de cada frame

    # Para salir del bucle, esperamos pulsación de la tecla D
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release() #Liberar dispositivo de captura
cv.destroyAllWindows() #Cerrar ventanas
