from classes142 import *

def main():
    p1 = Produto("Notebook", 8_500)
    p2 = Produto("Mouse", 250)
    p3 = Produto("Fone de Ouvido", 59.90)

    c1 = Carrinho()
    c1 = c1 + p1 + p2

    print(c1)

if __name__ == "__main__":
    main()