import json
import os
import tkinter as tk
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import buscar_eventos
from views import evento_details_view
import ubicacion_details_view

def mostrar_main_view():
    def mostrar_lista_eventos():
        ventana_lista = tk.Toplevel(root)
        ventana_lista.title("Lista de Eventos Disponibles")
        ventana_lista.geometry("800x600")

        # Cambiar el color de fondo a gris claro
        ventana_lista.configure(bg="#E5E5E5")

        # Crear una lista para mostrar los nombres de los eventos
        lista_eventos = tk.Listbox(ventana_lista)
        lista_eventos.pack()

        # Cargar los eventos desde el archivo eventos_data.json
        ruta_archivo = "data\eventos_data.json"
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r') as file:
                data = json.load(file)
            eventos = data["eventos"]

            # Agregar los nombres de los eventos a la lista
            for evento in eventos:
                lista_eventos.insert(tk.END, evento["nombre"])
        else:
            lista_eventos.insert(tk.END, "No se encontró el archivo eventos_data.json")

        def mostrar_detalle_ubicacion(evento_id):
            ubicacion_id = None
            # Obtener la ubicacion_id del evento seleccionado
            for evento in eventos:
                if evento["id"] == evento_id:
                    ubicacion_id = evento["id_ubicacion"]
                    break

            if ubicacion_id is not None:
                # Mostrar detalles de la ubicacion en ubicacion_details_view.py
                ubicacion_details_view.mostrar_ubicacion_details_view(ubicacion_id)

        # Vincular la funcion mostrar_detalle_ubicacion al evento de seleccion en la lista
        lista_eventos.bind("<Double-Button-1>", lambda event: mostrar_detalle_ubicacion(int(lista_eventos.curselection()[0])+1))


    root = tk.Tk()
    root.title("Tour Musical - Inicio")

    # Pantalla Completa
    root.attributes("-fullscreen", True)

    image = Image.open("C:\\Users\\fuerz\\OneDrive\\Imágenes\\Tour Musical\\Tour Musical Menu.jpg")
    background_image = ImageTk.PhotoImage(image)

    # Establecer el tamaño de la ventana principal al tamaño de la pantalla
    root.geometry(f"{1920}x{1080}")

    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Título principal
    titulo_label = tk.Label(root, text="¡Bienvenido a Tour Musical!",
                            font=("Roboto", 24), bg="#2F242C", fg="#E5E5E5")
    titulo_label.pack(pady=100)

    # Botones
    button_descubrir = tk.Button(root, text="Descubrir Eventos",
                                 font=("Open Sans", 14), bg="#E6D884",
                                 command=mostrar_lista_eventos)
    button_descubrir.pack(pady=50)

    button_buscar = tk.Button(root, text="Buscar Eventos",
                              font=("Open Sans", 14), bg="#E6D884",
                              command=buscar_eventos.buscar_eventos_musicales)
    button_buscar.pack(pady=50)

    button_historial = tk.Button(root, text="Historial de Eventos",
                                 font=("Open Sans", 14), bg="#E6D884",
                                 command=evento_details_view.mostrar_evento_details_view)
    button_historial.pack(pady=50)

    root.mainloop()

mostrar_main_view()