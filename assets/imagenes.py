from PIL import Image, ImageTk

def cargar_imagen_ruta(ruta):
    imagen = Image.open(ruta)
    return ImageTk.PhotoImage(imagen)