from contaBancaria import ContaBancaria

def main():
    cc = ContaBancaria(123, "Camilly", 800, "123456")
    cc.sacar(200)
    cc.depositar(1000)

if __name__ == "__main__":
    main()