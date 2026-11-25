from termostato import *
from rich import print

def main():
    t = Termostato()
    try:
        t.temperatura = 2
    except Exception as erro:
        print(f"Houve um erro: {erro}") 
    print(f"A temperatura atual é de {t.temperaturaFormatada}")

if __name__ == "__main__":
    main()