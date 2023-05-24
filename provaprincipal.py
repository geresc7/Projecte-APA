import cv2
from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image
import edicion_imagenes

def cargar_imagen():
    ruta_imagen = askopenfilename(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])
    if ruta_imagen:
        imagen = cv2.imread(ruta_imagen)
        imagen_editada = aplicar_funcionalidad(imagen, funcionalidad_var.get())
        mostrar_imagen(imagen_editada)
        edicion_imagenes.foto_dibuix(ruta_imagen)

def aplicar_funcionalidad(imagen, funcionalidad):
    if funcionalidad == "Escala de grises":
        imagen_editada = edicion_imagenes.aplicar_filtro_grises(imagen)
    elif funcionalidad == "Desenfoque":
        imagen_editada = edicion_imagenes.aplicar_filtro_blur(imagen)
    elif funcionalidad == "Dibuix":
        imagen_editada = edicion_imagenes.foto_dibuix(imagen)
    # Agrega más opciones de funcionalidad según tus necesidades
    return imagen_editada

def mostrar_imagen(imagen):
    ventana = Toplevel()
    ventana.title("Imagen Editada")
    ventana.configure(background="#F2F2F2")
    
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    imagen_pil = ImageTk.PhotoImage(Image.fromarray(imagen))
    etiqueta_imagen = Label(ventana, image=imagen_pil)
    etiqueta_imagen.pack(pady=10)

    ventana.mainloop()

root = Tk()
root.title("One Shot")
root.iconbitmap("Logo.ico")
root.configure(background="#F2F2F2")

frame_superior = Frame(root, bg="#F2F2F2")
frame_superior.pack()

label_titulo = Label(frame_superior, text="One Shot", font=("Arial", 24), bg="#F2F2F2")
label_titulo.pack(pady=10)

frame_botones = Frame(root, bg="#F2F2F2")
frame_botones.pack()

funcionalidad_var = StringVar()
funcionalidad_var.set("Escala de grises")

opcion_1 = Radiobutton(frame_botones, text="Escala de grises", variable=funcionalidad_var, value="Escala de grises", font=("Arial", 14), bg="#F2F2F2", activebackground="#F2F2F2", selectcolor="#F2F2F2")
opcion_1.pack(side=LEFT, padx=10)

opcion_2 = Radiobutton(frame_botones, text="Desenfoque", variable=funcionalidad_var, value="Desenfoque", font=("Arial", 14), bg="#F2F2F2", activebackground="#F2F2F2", selectcolor="#F2F2F2")
opcion_2.pack(side=LEFT, padx=10)

opcion_3 = Radiobutton(frame_botones, text="Dibuix", variable=funcionalidad_var, value="Dibuix", font=("Arial", 14), bg="#F2F2F2", activebackground="#F2F2F2", selectcolor="#F2F2F2")
opcion_3.pack(side=LEFT, padx=10)

boton_cargar = Button(root, text="Cargar Imagen", command=cargar_imagen, font=("Arial", 14), relief="flat", bg="#4CAF50", fg="white", activebackground="#45A049", activeforeground="white")
boton_cargar.pack(pady=20)

button_quit = Button(root, text="Salir del Programa", command=root.quit, font=("Arial", 14), relief="flat", bg="#F44336", fg="white", activebackground="#E53935", activeforeground="white")
button_quit.pack()

root.mainloop()
