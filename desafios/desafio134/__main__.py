from retangulo import Retangulo

def main():
    r = Retangulo()
    try:
        r.base = 12
        r.altura = 5
    except Exception as erro:
        print(f"Ocorreu um erro do tipo {type(erro).__name__}: {erro}")
        
    print(r.medidas)

if __name__ == "__main__":
    main()