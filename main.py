from abc import ABC, abstractmethod


class EntidadBase(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def salida(self):
        pass

    def ingreso(self):
        pass

    def precio(self):
        pass

    def reserva(self):
        pass

    def cancelar_reserva(self):
        pass

    def equipo(self):
        pass

    def tiempo(self):
        pass

    def descuento(self):
        pass
