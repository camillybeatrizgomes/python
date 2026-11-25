from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        frete = 0

    @abstractmethod
    def calcularFrete(self):
        pass


class Moto(Transporte):

    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcularFrete(self):
        self.frete = self.distancia * Moto.fator
        return f"R$ {self.frete:.2f}"
    

class Caminhao(Transporte):

    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcularFrete(self):
        if self.distancia < 50:
            self.frete = 0
            return "Raio Mínimo de 50 Km"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R$ {self.frete:.2f}"


class Drone(Transporte):

    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcularFrete(self):
        if self.distancia > 10:
            self.frete = 0
            return "Raio Máximo de 10 Km"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R$ {self.frete:.2f}"