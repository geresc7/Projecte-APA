import cv2
import numpy as np
from tkinter.filedialog import *
from tkinter import *


gui = Tk(className="Interfaz") #variable tipo tkinter (interfaz)
gui.geometry("400x500") #tamany finestra interfaz creo

foto = askopenfilename() #triar foto
img = cv2.read(foto) #llegir la imatge
res = cv2.resize(img, dsize=(400,400), interpolation=cv2.INTER_CUBIC) #ns que fa

gris = cv2.cvtColor (img, cv2.COLOR)