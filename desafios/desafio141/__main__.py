from classes141 import *

def main():
    u = [Usuario("Camilly", "camilly@gmail.com"), Usuario("Gabriela", "gabi@gmail.com")]
    a = [Aluno("Beatriz", "Administração", "2 ano"), Aluno("Carol", "História", "3 ano"), Aluno("Felipe", "Tecnologia", "3 ano")]

    exportarDados(JSON(), u)
    exportarDados(XML(), a)

if __name__ == "__main__":
    main()