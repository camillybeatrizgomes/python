# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto() # 1º Objeto da Classe Gafanhoto
g1.nome = "Maria"
g1.idade = 19
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto() # 2º Objeto da Classe Gafanhoto
g2.nome = "Beatriz"
g2.idade = 33
g2.aniversario()
print(g2.mensagem())