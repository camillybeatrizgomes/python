estado = dict()
brasil = list()
for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla de Estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for chave, valor in estado.items():
        print(f'O campo {chave} tem valor {valor}.')
