from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    @abstractmethod
    def obtener_tipo_usuario(self):
        pass
