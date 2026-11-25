from diario import *
from rich import print

def main():
    d = Diario()
    d.escrever("Gosto muito de Pizza!")
    d.escrever("Estou estudando Python")
    d.senha = "8890"

    try:
        d.ler("8890")
    except Exception as erro:
        print(f"[red]ERRO: {erro}[/]")

if __name__ == "__main__":
    main()