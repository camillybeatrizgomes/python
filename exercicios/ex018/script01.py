def fatorial(num = 1):
    f = 1
    for contador in range(num, 0, -1):
        f *= contador
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')