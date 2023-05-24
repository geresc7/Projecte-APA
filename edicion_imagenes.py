import cv2
import numpy as np

def aplicar_filtro_grises(imagen):
    # Aplicar filtro de escala de grises a la imagen
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return imagen_gris

def aplicar_filtro_blur(imagen):
    # Aplicar filtro de desenfoque a la imagen
    imagen_blur = cv2.blur(imagen, (5, 5))
    return imagen_blur


def foto_dibuix(imagen):
    #img = cv2.imread(imagen) #llegir la imatge
    res = cv2.resize(imagen, dsize=(400,400), interpolation=cv2.INTER_CUBIC) #ns que fa

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) #canviar color a gris
    gris = cv2.medianBlur(gris, 3) #suavitzar
    bordes = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(imagen, 9, 250, 250)
    dibuix = cv2.bitwise_and(color, color, mask=bordes)
    return bordes

