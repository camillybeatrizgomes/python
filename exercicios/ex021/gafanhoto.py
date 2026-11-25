# Declaração de Classe
class Gafanhoto:
    """
        Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.
        Para criar uma nova pessoa, use:

        variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} | idade = {self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("Maria", 19) # 1º Objeto da Classe Gafanhoto
g1.aniversario()
print(g1)

g2 = Gafanhoto("Beatriz", 33) # 2º Objeto da Classe Gafanhoto
g2.aniversario()
print(g2.__dict__) # Atributo que traz os dados em um dicionário
print(g2.__getstate__()) # Método que traz o estado do abjeto

print(g1.__doc__) # Dunder Attribute
# Responsável por acessar a documentação (docstring) de um objeto, como funções, métodos, classes ou módulos.