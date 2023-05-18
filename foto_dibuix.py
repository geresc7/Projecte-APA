import cv2
import numpy as np
from tkinter.filedialog import *
from tkinter import *

inte = Tk(className = "exemple")
inte.geometry("500x500")

foto = askopenfilename() #triar foto
img = cv2.read(foto) #llegir la imatge
res = cv2.resize(img, dsize=(400,400), interpolation=cv2.INTER_CUBIC) #ns que fa

gris = cv2.cvtColor (img, cv2.COLOR)#canviar color a gris
gris = cv2.medianBlur (gris, 3) #suavitzar
bordes = cv2.adaptiveThreshold (gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)




