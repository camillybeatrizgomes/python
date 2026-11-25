from abc import ABC, abstractmethod # Abstract Base Classes

class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazerAniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

# Classe Aluno herda da classe Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazerMatricula(self):
        print(f"{self.nome} acabou de fazer matricula.")

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso} na turma {self.turma}")

# Classe Professor herda da classe Pessoa
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        print(f"Prof. {self.nome} começou a dar aula.")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} no {self.nivel}")

# Classe Funcionario herda da classe Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def baterPonto(self):
        print(f"{self.nome} acabou de bater o ponto.")

    def estudar(self):
        print(f"{self.nome} se especializa para a área de {self.setor}")