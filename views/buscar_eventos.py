import tkinter as tk
from tkinter import ttk
import json

#Cargar los eventos desde el archivo eventos_data.json
ruta_archivo = "data\eventos_data.json"
with open(ruta_archivo, 'r') as file:
    data = json.load(file)
eventos = data["eventos"]

# Declarar las variables globales
entry_nombre = None
entry_artista = None
entry_genero = None
resultado_text = None

#Recorro el diccionario en búsqueda de coincidencia de criterios 
def buscar_eventos(criterios):
    resultados = []
    for evento in eventos:
        cumple_criterios = True
        for criterio, valor in criterios.items():
            if valor and str(valor).lower() not in str(evento[criterio]).lower():
                cumple_criterios = False
                break
        if cumple_criterios:
            resultados.append(evento)
    return resultados

#Permite ingresar los criterios de búsqueda
def mostrar_resultados():
    criterios = {
        "nombre": entry_nombre.get(),
        "artista": entry_artista.get(),
        "genero": entry_genero.get(),
    }
    #Llama la función buscar_eventos
    eventos_encontrados = buscar_eventos(criterios)
    
    if eventos_encontrados:
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete(1.0, tk.END)
        for evento in eventos_encontrados:
            resultado_text.insert(tk.END, f"Nombre: {evento['nombre']}\nArtista: {evento['artista']}\nGénero: {evento['genero']}\n\n")
        resultado_text.config(state=tk.DISABLED)
    else:
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "No se encontró un evento que cumpla con sus criterios. Pruebe ingresando otro/s.")
        resultado_text.config(state=tk.DISABLED)

#Función 
def buscar_eventos_musicales():
    global entry_nombre, entry_artista, entry_genero, resultado_text

    root = tk.Tk()
    root.title("Buscador de Eventos Musicales")
    root.geometry("500x400")

    label_instrucciones = tk.Label(root, text="Ingrese los criterios de búsqueda para encontrar eventos musicales:")
    label_instrucciones.pack(pady=10)

    entry_nombre = tk.Entry(root, width=30)
    entry_nombre.pack(pady=5)

    entry_artista = tk.Entry(root, width=30)
    entry_artista.pack(pady=5)

    entry_genero = tk.Entry(root, width=30)
    entry_genero.pack(pady=5)

    button_buscar = tk.Button(root, text="Buscar Eventos", command=mostrar_resultados)
    button_buscar.pack(pady=10)

    resultado_text = tk.Text(root, width=60, height=10, state=tk.DISABLED)
    resultado_text.pack(pady=10)

    root.mainloop()

buscar_eventos_musicales()