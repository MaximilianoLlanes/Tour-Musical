import tkinter as tk

def mostrar_evento_details_view():
    root = tk.Tk()
    root.title("Detalles del Evento")

    # Aquí puedes crear y configurar los elementos de la interfaz
    label_nombre = tk.Label(root, text="Nombre del Evento:")
    label_nombre.pack()

    label_artista = tk.Label(root, text="Artista:")
    label_artista.pack()

    label_genero = tk.Label(root, text="Género Musical:")
    label_genero.pack()

    label_ubicacion = tk.Label(root, text="Ubicación:")
    label_ubicacion.pack()

    label_hora_inicio = tk.Label(root, text="Hora de Inicio:")
    label_hora_inicio.pack()

    label_hora_fin = tk.Label(root, text="Hora de Fin:")
    label_hora_fin.pack()

    label_descripcion = tk.Label(root, text="Descripción:")
    label_descripcion.pack()

    root.mainloop()