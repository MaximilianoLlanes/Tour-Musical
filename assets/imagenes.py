from PIL import Image, ImageTk

#Sin usar

def cargar_imagen_ruta(ruta):
    imagen = Image.open(ruta)
    return ImageTk.PhotoImage(imagen)