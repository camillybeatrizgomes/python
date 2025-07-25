pessoas = {'nome': 'Camilly', 'sexo': 'F', 'idade': 21}
pessoas['nome'] = 'Beatriz'
pessoas['peso'] = 85.5
del pessoas['sexo']
for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')