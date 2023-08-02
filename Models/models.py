import json

class Evento:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    def guardar_en_archivo(self, archivo):
        with open(archivo, "w") as archivo_evento:
            json.dump(self.__dict__, archivo_evento)

    @classmethod
    def cargar_desde_archivo(cls, archivo):
        with open(archivo, "r") as archivo_evento:
            data = json.load(archivo_evento)
            return cls(**data)

class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

class Usuario:
    def __init__(self, id, nombre, apellido, historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos

class Resena:
    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
