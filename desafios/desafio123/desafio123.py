import math

from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelha" | "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.estaTampada = True

    def escrever(self, mensagem):
        if self.estaTampada:
            print(f":prohibited: A {self.cor}caneta [/]está tampada.")
        else:
            print(f"{self.cor}{mensagem}[/] ", end="")
    
    def quebrarLinha(self, quantidade):
        print("\n" * quantidade, end="")

    def tampada(self):
        self.estaTampada = True  

    def destampada(self):
        self.estaTampada = False

c1 = Caneta("vermelha")
c2 = Caneta("azul")
c3 = Caneta("rosa")

c1.escrever("Como vai?")

c2.destampada()
c2.escrever("Olá, mundo")
c2.tampada()
c2.escrever("Estudando Python")

c3.destampada()
c3.quebrarLinha(3)
c3.escrever("Funcionou?")
