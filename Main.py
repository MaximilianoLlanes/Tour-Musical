import tkinter as tk
from tkinter import messagebox
import os
import sys

# Agregar el directorio "views" al PYTHONPATH
views_dir = os.path.join(os.path.dirname(__file__), "Views")
sys.path.append(views_dir)

# Agregar el directorio actual al PYTHONPATH
current_dir = os.path.dirname(__file__)
sys.path.append(current_dir)

# Importar las funciones para mostrar las vistas desde la carpeta "views"
from main_view import mostrar_main_view
from evento_details_view import mostrar_evento_details_view
from ubicacion_details_view import mostrar_ubicacion_details_view

# Función para mostrar el menú principal
def mostrar_menu_principal():
    """Mostrar el menú principal de la aplicación."""
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    opcion = tk.messagebox.askquestion("Deseas cerrar la aplicación?",
                                       "¿Deseas cerrar la aplicación?",
                                       icon="question")

    if opcion == "yes":
        root.destroy()  # Cerrar la ventana principal
    elif opcion == "no":
        mostrar_main_view()
    else:
        mostrar_ubicacion_details_view()

# Función principal para ejecutar la aplicación
def main():
    mostrar_menu_principal()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

def mostrar_menu_principal():
    """Mostrar el menú principal de la aplicación."""
    root = tk.Tk()

    def cerrar_ventana():
        # Pregunta al usuario si desea cerrar la ventana
        if messagebox.askokcancel("Cerrar ventana", "¿Estás seguro de que deseas salir?"):
            root.destroy()  # Cierra la ventana y termina el programa

    root.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Define el evento de cierre de la ventana

    # Aquí iría el resto de la configuración y elementos de la interfaz
    # ...

    root.mainloop()

if __name__ == "__main__":
    mostrar_menu_principal()

#Esto es una prueba
