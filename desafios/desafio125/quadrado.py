from poligono import Poligono

class Quadrado(Poligono):

    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    # Método (perímetro)
    def perimetro(self):
        return self.lado * 4
    
    # Método (área)
    def area(self):
        return self.lado ** 2