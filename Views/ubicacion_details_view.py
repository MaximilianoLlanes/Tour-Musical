import tkinter as tk

def mostrar_ubicacion_details_view():
    root = tk.Tk()
    root.title("Detalles de la Ubicación")

    # Completar: crear y configurar los elementos de la interfaz
    label_nombre = tk.Label(root, text="Nombre de la Ubicación:")
    label_nombre.pack()

    label_direccion = tk.Label(root, text="Dirección:")
    label_direccion.pack()

    label_coordenadas = tk.Label(root, text="Coordenadas:")
    label_coordenadas.pack()

    root.mainloop()