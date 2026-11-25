from poligono import Poligono
from math import pi

class Circulo(Poligono):

    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    # Método (perímetro)
    def perimetro(self):
        return 2 * pi * self.raio
    
    # Método (área)
    def area(self):
        return pi * (self.raio ** 2)