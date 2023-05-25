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

def aplicar_funcionalidad(imagen, funcionalidad):
    if funcionalidad == "Escala de grises":
        imagen_editada = edicion_imagenes.aplicar_filtro_grises(imagen)
    elif funcionalidad == "Desenfoque":
        imagen_editada = edicion_imagenes.aplicar_filtro_blur(imagen)
    elif funcionalidad == "Dibuix":
        imagen_editada = edicion_imagenes.foto_dibuix(imagen)
    elif funcionalidad == "Dibuix Color":
        imagen_editada = edicion_imagenes.foto_dibuix_color(imagen)
    # Agrega más opciones de funcionalidad según tus necesidades
    return imagen_editada


def mostrar_imagen(imagen):
      
    dimensions = imagen.shape
    height = int(imagen.shape[0])
    width = int(imagen.shape[1])
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    while height > 800:
        width = int(width/2)
        height = int(height/2)
        cv2.resizeWindow('image', width, height)
    cv2.imshow('image', imagen)

def guardar_imagen(imagen):
        ruta_guardar = asksaveasfilename(filetypes=[("Archivo JPEG", "*.jpg"), ("Archivo PNG", "*.png"), ("Archivo BMP", "*.bmp")])
        if ruta_guardar:
            formato = ruta_guardar.split(".")[-1]  # Obtener la extensión del archivo
            cv2.imwrite(ruta_guardar, cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 90]) if formato == "jpg" else cv2.imwrite(ruta_guardar, cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR))

root = Tk()
root.title("One Shot")
root.iconbitmap("Logoico.ico")

my_img = ImageTk.PhotoImage(Image.open("Photomatobo.png"))
my_label = Label (image=my_img)
my_label.pack()
root.configure(background="#F2F2F2")

frame_superior = Frame(root, bg="#F2F2F2")
frame_superior.pack()

frame_botones = Frame(root, bg="#F2F2F2")
frame_botones.pack()

funcionalidad_var = StringVar()
funcionalidad_var.set("Escala de grises")

opcion_1 = Radiobutton(frame_botones, text="Escala de grises", variable=funcionalidad_var, value="Escala de grises", font=("Calibri light", 14), bg="#F2F2F2", activebackground="#F2F2F2", selectcolor="#F2F2F2")
opcion_1.pack(side=LEFT, padx=10)

opcion_2 = Radiobutton(frame_botones, text="Desenfoque", variable=funcionalidad_var, value="Desenfoque", font=("Calibri light", 14), bg="#F2F2F2", activebackground="#F2F2F2", selectcolor="#F2F2F2")
opcion_2.pack(side=LEFT, padx=10)

opcion_3 = Radiobutton(frame_botones, text="Dibuix", variable=funcionalidad_var, value="Dibuix", font=("Calibri light", 14), bg="#F2F2F2", activebackground="#F2F2F2", selectcolor="#F2F2F2")
opcion_3.pack(side=LEFT, padx=10)

opcion_4 = Radiobutton(frame_botones, text="Dibuix Color", variable=funcionalidad_var, value="Dibuix Color", font=("Calibri light", 14), bg="#F2F2F2", activebackground="#F2F2F2", selectcolor="#F2F2F2")
opcion_4.pack(side=LEFT, padx=10)

boton_cargar = Button(root, text="Cargar Imagen", command=cargar_imagen, font=("Calibri light", 14), relief="flat", bg="#4CAF50", fg="white", activebackground="#45A049", activeforeground="white")
boton_cargar.pack(side=LEFT, padx=10)

boton_guardar = Button(root, text="Guardar Imagen", command=guardar_imagen, font=("Calibri light", 14), relief="flat", bg="#4CBF50", fg="white", activebackground="#45A049", activeforeground="white")
boton_guardar.pack(side=LEFT, padx=10)

button_quit = Button(root, text="Salir del Programa", command=root.quit, font=("Calibri light", 14), relief="flat", bg="#F44336", fg="white", activebackground="#E53935", activeforeground="white")
button_quit.pack(pady=10, anchor=CENTER)


root.mainloop()