matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceiraColuna = maiorSegundaLinha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 25)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
    print()
print('-=' * 25)
print(f'A soma dos valores pares é {somaPares}')
for linha in range(0, 3):
    somaTerceiraColuna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}')
for coluna in range(0, 3):
    if coluna == 0:
        maiorSegundaLinha = matriz[1][coluna]
    elif matriz[1][coluna] > coluna:
        maiorSegundaLinha = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorSegundaLinha}')
