from abc import ABC,abstractmethod

class Widget(ABC):

    @abstractmethod
    def show(self):
        """Mostrar el widget"""
        pass

    @abstractmethod
    def logic(self):
        """logica del widget"""
        pass

    @abstractmethod
    def unshow(self):
        """Ocultar el widget"""
        pass