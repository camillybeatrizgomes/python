from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, quantidadeDeLados):
        self.quantidadeDeLados = quantidadeDeLados
    
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass