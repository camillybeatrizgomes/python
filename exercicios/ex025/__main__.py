from rich import print, inspect
from ex025 import Avaliacao

def main():
    a1 = Avaliacao("Pedro", "Matemática", 9)
    a1.set_nota(8.7)
    print(f"{a1.nome} tirou {a1.get_nota()} em {a1.disciplina}")
    inspect(a1, private=True)

if __name__ == "__main__":
    main()