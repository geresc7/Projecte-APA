import cv2
import numpy as np
from tkinter.filedialog import *
from tkinter import *

def foto_dibuix(foto):
    inte = Tk(className = "exemple")
    inte.geometry("500x500")

    img = cv2.imread(foto) #llegir la imatge
    res = cv2.resize(img, dsize=(400,400), interpolation=cv2.INTER_CUBIC) #ns que fa

    gris = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)#canviar color a gris
    gris = cv2.medianBlur (gris, 3) #suavitzar
    bordes = cv2.adaptiveThreshold (gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(img, 9, 250, 250)
    dibuix = cv2.bitwise_and(color, color, mask=bordes)

    cv2.imshow("imatge", img)
    cv2.imshow("contorns", bordes)
    cv2.imshow("dibuix", dibuix)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

