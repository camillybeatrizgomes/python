from classes import * 

def main():
    a = Numero(11)
    b = Texto("Camilly")
    c = Lista([1, 2, 3])
    d = Papel()
    e = Casa()

    tentarDobrar(a)
    tentarDobrar(b)
    tentarDobrar(c)
    # tentarDobrar(d)
    tentarDobrar(e)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

if __name__ == "__main__":
    main()