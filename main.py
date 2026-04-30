from abc import ABC, abstractmethod

# Clase base abstracta que define la estructura de las entidades en el sistema


class EntidadBase(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def salida(self):
        pass

    @abstractmethod
    def ingreso(self):
        pass

    @abstractmethod
    def precio(self):
        pass

    @abstractmethod
    def reserva(self):
        pass

    @abstractmethod
    def cancelar_reserva(self):
        pass

    @abstractmethod
    def equipo(self):
        pass

    @abstractmethod
    def tiempo(self):
        pass

    @abstractmethod
    def descuento(self):
        pass

    @abstractmethod
    def validar_datos(self):
        pass

    @abstractmethod
    def registrar_cliente(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass
