import tkinter as tk
from tkinter import messagebox
import os
import sys

# Agregar el directorio "views" al PYTHONPATH
views_dir = os.path.join(os.path.dirname(__file__), "Views")
sys.path.append(views_dir)

# Importar los módulos desde la carpeta "views"
from main_view import mostrar_main_view
from evento_details_view import mostrar_evento_details_view
from ubicacion_details_view import mostrar_ubicacion_details_view

# Importar las funciones para mostrar las vistas desde la carpeta "views"
from main_view import mostrar_main_view
from evento_details_view import mostrar_evento_details_view
from ubicacion_details_view import mostrar_ubicacion_details_view

# Función para mostrar el menú principal
def mostrar_menu_principal():
    """Mostrar el menú principal de la aplicación."""
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    opcion = tk.messagebox.askquestion("Menú Principal",
                                       "¿Qué acción deseas realizar?",
                                       icon="question")

    if opcion == "yes":
        mostrar_main_view()
    elif opcion == "no":
        mostrar_evento_details_view()
    else:
        mostrar_ubicacion_details_view()

# Función principal para ejecutar la aplicación
def main():
    mostrar_menu_principal()

if __name__ == "__main__":
    main()