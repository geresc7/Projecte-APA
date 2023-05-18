import cv2
import numpy as np
from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("One Shot")
root.iconbitmap("Logo.ico")

my_img = ImageTk.PhotoImage(Image.open("nom_imatge.png"))
my_label = Label (image=my_img)
my_label.pack()

button_quit = Button(root, text="Sortir del programa", command=root.quit)
button_quit.pack()

root.mainloop()