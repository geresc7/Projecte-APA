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

# Agrega más funciones de edición de imágenes según tus necesidades
