from rich import print, inspect
from ex026 import Avaliacao

def main():
    a1 = Avaliacao("Pedro", "Matemática", 9)
    a1.nota = 8.7
    print(f"{a1.nome} tirou {a1.nota} em {a1.disciplina}")
    inspect(a1, private=True)

if __name__ == "__main__":
    main()