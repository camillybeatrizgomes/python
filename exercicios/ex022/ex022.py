from rich import print, inspect

class Pessoa:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazerAniversario(self):
        self.idade += 1

# Classe Aluno herda da classe Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazerMatricula(self):
        print(f"{self.nome} acabou de fazer matricula.")

# Classe Professor herda da classe Pessoa
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        print(f"Prof. {self.nome} começou a dar aula.")

# Classe Funcionario herda da classe Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def baterPonto(self):
        print(f"{self.nome} acabou de bater o ponto.")

a1 = Aluno("José", 17, "Informática", "T01")
a1.fazerAniversario()
a1.fazerMatricula()
inspect(a1, methods=True)

p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
p1.darAula()
inspect(p1, methods=True)

f1 = Funcionario("Carlos", 28, "Vendedor", "Vendas")
f1.baterPonto()
f1.fazerAniversario()
inspect(f1, methods=True)