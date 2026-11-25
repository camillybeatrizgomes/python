from rich import print, inspect
from aluno import Aluno
from funcionario import Funcionario
from professor import Professor

def main():
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

if __name__ == "__main__":
    main()