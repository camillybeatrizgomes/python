from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod

class Funcionario(ABC):
    salarioMinimo = 1_612
    descontoINSS = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.salarioBruto = 0
        self.salario = 0

    @abstractmethod
    def calcularSalario(self):
        pass

    def analisarSalario(self):
        calculo = self.salario / Funcionario.salarioMinimo

        mensagem = f"O salário de [blue]{self.nome}[/] ([magenta]{self.__class__.__name__}[/]) [green]R$ {self.salario:.2f}[/] e corresponde a [yellow]{calculo:.1f} salários mínimos[/]"
        painel = Panel(mensagem, title="Análise de Salário", width=50)
        print(painel)


class FuncionarioHorista(Funcionario):
    def __init__(self, nome=None, valorPorHora = 7.37, horasTrabalhadas = 220):
        super().__init__(nome)
        self.valorPorHora = valorPorHora
        self.horasTrabalhadas = horasTrabalhadas
        self.salarioBruto = self.valorPorHora * self.horasTrabalhadas

    def calcularSalario(self):
        self.salario = self.salarioBruto - (self.salarioBruto * Funcionario.descontoINSS / 100)

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome=None, salarioBruto = Funcionario.salarioMinimo):
        super().__init__(nome)
        self.salarioBruto = salarioBruto

    def calcularSalario(self):
        self.salario = self.salarioBruto - (self.salarioBruto * Funcionario.descontoINSS / 100)
