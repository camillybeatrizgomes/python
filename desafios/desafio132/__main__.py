from credencial import Credencial

def main():
    c = Credencial()
    c.senha = str(input("Digite sua senha: "))
    print(c.senha)
    c.validar("camilly")

if __name__ == "__main__":
    main()
