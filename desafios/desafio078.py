listaNumeros = list()
maior = menor = 0
for cont in range(0, 5):
    listaNumeros.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = listaNumeros[cont]
    else:
        if listaNumeros[cont] > maior:
            maior = listaNumeros[cont]
        if listaNumeros[cont] < menor:
            menor = listaNumeros[cont]
print(f'Você digitou os valores {listaNumeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(listaNumeros):
    if valor == maior:
        print(f'{indice}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(listaNumeros):
    if valor == menor:
        print(f'{indice}...', end=' ')
