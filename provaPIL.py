from PIL import Image   #llibreria PILLOW
import os

image1 = Image.open('nom_imatge.jpg') #obrir imatge
image1.show()

image1.save('nom_imatge2.png') #guarda imatge (es pot passar de jpg a png, pero no al reves)