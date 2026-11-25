# pessoas = {'nome': 'Camilly', 'sexo': 'F', 'idade': 21}
# print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')

# -----------------------------
# pessoas = {'nome': 'Camilly', 'sexo': 'F', 'idade': 21}
# pessoas['nome'] = 'Beatriz'
# pessoas['peso'] = 85.5
# del pessoas['sexo']
# for chave, valor in pessoas.items():
#     print(f'{chave} = {valor}')

# -----------------------------
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[1]['sigla'])

# -----------------------------
estado = dict()
brasil = list()
for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla de Estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for chave, valor in estado.items():
        print(f'O campo {chave} tem valor {valor}.')

