from classes136 import *

def main():
    f = Designer("Ana", 8_000)
    try: 
        f.salario = 2_000
    except Exception as erro:
        print(f"ERRO: {erro}")
    print(f)

if __name__ == "__main__":
    main()
