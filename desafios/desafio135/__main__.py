from classes135 import *

def main():
    a1 = Aluno("Ana", 1998, "ADS")
    a1._nascimento = 2001
    a1.adicionarCurso("ENG")

    print(a1.__dict__)

if __name__ == "__main__":
    main()