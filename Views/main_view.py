import tkinter as tk
from tkinter import ttk
from views import evento_details_view

def mostrar_main_view():
    root = tk.Tk()
    root.title("Tour Musical - Inicio")
    root.geometry("400x300")  # Ajusta el tamaño de la ventana según tus preferencias

    # Cambiar el color de fondo a gris claro
    root.configure(bg="#E5E5E5")

    # Título principal en púrpura oscuro
    titulo_label = tk.Label(root, text="¡Bienvenido a Tour Musical!",
                            font=("Roboto", 24), bg="#2F242C", fg="#E5E5E5")
    titulo_label.pack(pady=20)

    # Botones personalizados con color amarillo para resaltar
    button_descubrir = tk.Button(root, text="Descubrir Eventos",
                                 font=("Open Sans", 14), bg="#E6D884",
                                 command=evento_details_view.mostrar_evento_details_view)
    button_descubrir.pack(pady=10)

    button_buscar = tk.Button(root, text="Buscar Eventos",
                              font=("Open Sans", 14), bg="#E6D884",
                              command=evento_details_view.mostrar_evento_details_view)
    button_buscar.pack(pady=10)

    button_historial = tk.Button(root, text="Historial de Eventos",
                                 font=("Open Sans", 14), bg="#E6D884",
                                 command=evento_details_view.mostrar_evento_details_view)
    button_historial.pack(pady=10)

    root.mainloop()

mostrar_main_view()