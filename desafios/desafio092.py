from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-' * 25)
for chave, valor in dados.items():
    print(f'    - {chave} tem o valor {valor}')
