from ex024 import ContaBancaria

# Encapsulamento: atributos internos devem ser usados com cuidado.
# Regra: use métodos da classe para alterar estado, não mude atributos privados direto.
# Não faça acesso direto em atributos "protegidos" ou "privados".
# Isso quebra a integridade da classe e vai contra o encapsulamento.

def main():
    c1 = ContaBancaria("111", "Maria", 3_000)
    c1.depositar(1_000)
    c1._titular = "Pedro"  # É possível alterar, mesmo sendo protegido, mas não é recomendado.
    c1._ContaBancaria__saldo = 0  # Também pode ser alterado, mas não é recomendado. Isso quebra o encapsulamento.
    print(c1)

if __name__ == "__main__":
    main()