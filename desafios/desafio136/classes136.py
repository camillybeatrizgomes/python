from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome:str = None, salario:float = 1_621):
        self.nome = nome
        self.__salario = salario

    @abstractmethod
    def calcularBonus(self):
        pass

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario:float = None):
        if salario is None:
            raise ValueError("Impossível reajustar o salário desse jeito!")
        else:
            if salario >= self.__salario:
                self.__salario = salario
            else:
                raise ValueError("Você não pode reduzir o salário de um funcionário.")

    def __str__(self):
        return f"{self.nome} ganha R$ {self.salario:,.2f} e o bônus será de R$ {self.calcularBonus():,.2f}"

class Gerente(Funcionario):
    def __init__(self, nome="", salario=0):
        super().__init__(nome, salario)

    def calcularBonus(self):
        return self.salario * 0.15

class Designer(Funcionario):
    def __init__(self, nome = None, salario = 1621):
        super().__init__(nome, salario)

    def calcularBonus(self):
        return self.salario * 0.08

class Desenvolvedor(Funcionario):
    def __init__(self, nome = None, salario = 1621):
        super().__init__(nome, salario)

    def calcularBonus(self):
        return self.salario * 0.10
