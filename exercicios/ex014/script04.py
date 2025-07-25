valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for indice, valor in enumerate(valores):
    print(f'Na posição {indice} encontrei o valor {valor}')
print('Cheguei ao final da lista.')