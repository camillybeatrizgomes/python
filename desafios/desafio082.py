listaNumeros = []
listaPares = []
listaImpares = []
while True:
    listaNumeros.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [N / S] ')).strip().upper()[0]
    if resp in 'Nn':
        break
for indice, valor in enumerate(listaNumeros):
    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)
print('-=' * 25)
print(f'Lista completa é {listaNumeros}')
print(f'Lista de números pares é {listaPares}')
print(f'Lista de números ímpares é {listaImpares}')
