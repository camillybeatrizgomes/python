from funcionarios import FuncionarioHorista, FuncionarioMensalista

def main():
    f1 = FuncionarioHorista("José da Silva", 12, 190)
    f1.calcularSalario()
    f1.analisarSalario()

    f2 = FuncionarioMensalista("Maria Eduarda", 5300)
    f2.calcularSalario()
    f2.analisarSalario()

if __name__ == "__main__":
    main()