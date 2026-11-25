from classes137 import *

def main():
    a1 = DOC("teste", 1_200_000)
    abrirArquivo(a1)

    a2 = PDF("documento", 2_100_000)
    abrirArquivo(a2)

    a3 = PSD("image", 3_500_000)
    abrirArquivo(a3)

if __name__ == "__main__":
    main()