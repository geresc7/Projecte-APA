import cv2
from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image
import edicion_imagenes

def cargar_imagen():
    ruta_imagen = askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
    if ruta_imagen:
        imagen = cv2.imread(ruta_imagen)
        imagen_editada = edicion_imagenes.aplicar_filtro_grises(imagen)
        mostrar_imagen(imagen_editada)

def mostrar_imagen(imagen):
    ventana = Toplevel()
    ventana.title("Imagen Editada")
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    imagen_pil = ImageTk.PhotoImage(Image.fromarray(imagen))
    etiqueta_imagen = Label(ventana, image=imagen_pil)
    etiqueta_imagen.pack()
    ventana.mainloop()

root = Tk()
root.title("One Shot")
root.iconbitmap("Logo.ico")

frame_superior = Frame(root)
frame_superior.pack()

label_titulo = Label(frame_superior, text="One Shot")
label_titulo.config(font=("Arial", 24))
label_titulo.pack(pady=10)

frame_imagen = Frame(root)
frame_imagen.pack()

my_img = ImageTk.PhotoImage(Image.open("nom_imatge.png"))
my_label = Label(frame_imagen, image=my_img)
my_label.pack(pady=10)

frame_botones = Frame(root)
frame_botones.pack()

boton_cargar = Button(frame_botones, text="Cargar Imagen", command=cargar_imagen)
boton_cargar.pack(side=LEFT, padx=10)

button_quit = Button(frame_botones, text="Salir del Programa", command=root.quit)
button_quit.pack(side=RIGHT, padx=10)

root.mainloop()
