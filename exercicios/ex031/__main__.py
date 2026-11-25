from classes import Carteira

def main():
    c1 = Carteira(100)
    c2 = Carteira(100)
    c1 += 50
    print(c1)
    print(c1 == c2)

if __name__ == "__main__":
    main()