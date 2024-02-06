from rembg import remove
import tkinter as tk
from tkinter import filedialog as fdl

def vaciarFondo(imagenEntrada):
    imagenSalida=fdl.askdirectory()+"/imagenSinFondo.jpg"
    print(imagenSalida)
    with open(imagenEntrada, 'rb') as i:
        with open(imagenSalida, 'wb') as o:
            entradadatos = i.read()
            salidadatos = remove(entradadatos)
            o.write(salidadatos) 

def imagenReferencia():
    global entrada
    entrada=fdl.askopenfilename()
    print("Nombre del archivo seleccionado:", entrada)

def imagensinFondo():
    if entrada:
            vaciarFondo(entrada)

root = tk.Tk()
root.title("Vaciar fondo de imagen")
root.geometry("250x160")


boton = tk.Button(root, text="Seleccionar archivo", command=imagenReferencia)

boton2 = tk.Button(root, text="Guardar imagen sin fondo", command=imagensinFondo)


boton2.pack(ipadx=10,ipady=10)
boton.pack(ipadx=10, ipady=10)


root.mainloop()
