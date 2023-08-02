import tkinter as tk

from evento_details_view import mostrar_evento_details_view

def mostrar_main_view():
    root = tk.Tk()
    root.title("Vista Principal - Aplicación de Tour Musical")

    label_titulo = tk.Label(root, text="Eventos Musicales")
    label_titulo.pack()

    #Lista - ejemplo
    eventos = ["Evento 1", "Evento 2", "Evento 3"]
    listbox_eventos = tk.Listbox(root)
    for evento in eventos:
        listbox_eventos.insert(tk.END, evento)
    listbox_eventos.pack()    
    
    # Botón para ver detalles del evento
    button_detalles_evento = tk.Button(root, text="Ver Detalles del Evento", command=mostrar_evento_details_view)
    button_detalles_evento.pack()

    # Crear widgets de la interfaz
    titulo_label = tk.Label(root, text="🎵 Tour Musical 🎵", font=("Roboto", 20), padx=10, pady=10)
    indice_btn = tk.Button(root, text="Índice de Eventos", command=mostrar_indice_eventos)
    buscar_btn = tk.Button(root, text="Buscar y Filtrar Eventos", command=mostrar_buscar_eventos)
    historial_btn = tk.Button(root, text="Historial de Eventos Asistidos", command=mostrar_historial_eventos)

    # Ubicar los widgets en la interfaz
    titulo_label.pack()
    indice_btn.pack()
    buscar_btn.pack()
    historial_btn.pack()

    root.mainloop()

def mostrar_indice_eventos():
    # Completar: Aquí se mostraría la interfaz para el índice de eventos
    pass

def mostrar_buscar_eventos():
    # Completar: Aquí se mostraría la interfaz para buscar y filtrar eventos
    pass

def mostrar_historial_eventos():
    # Completar: Aquí se mostraría la interfaz para el historial de eventos asistidos
    pass

if __name__ == "__main__":
    mostrar_main_view()
