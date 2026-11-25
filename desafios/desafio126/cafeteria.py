from abc import ABC, abstractmethod

# Classe abstrata que define o template para preparar bebidas quentes
class BebidaQuente(ABC):
    def preparar(self):
        print("--- Iniciando o preparo ---")
        self.ferverAgua()
        self.misturar()
        self.servir()
        print("--- Bebida pronta! ---\n")

    def ferverAgua(self):
        print("1. Fervendo água a 100 graus Celsius.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

# Classe Cafe que herda de BebidaQuente e implementa os métodos abstratos
class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print("3. Servindo em xícara pequena.")

# Classe Cha que herda de BebidaQuente e implementa os métodos abstratos
class Cha(BebidaQuente):
    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água quente.")

    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.")

# Classe Leite que herda de BebidaQuente e implementa os métodos abstratos
class Leite(BebidaQuente):
    def misturar(self):
        print("2. Passando água pressurizada pelo bico do leite.")

    def servir(self):
        print("3. Servindo na caneca grande, já com café.")