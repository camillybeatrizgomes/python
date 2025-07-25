galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M / F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [N / S] ')).strip().upper()[0]
        if resp in 'NS':
            break
        print('ERRO! responda apenas N ou S.')
    if resp == 'N':
        break
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas.')
media = soma / len(galera)
print(f'B) A média das idades é de {media:5.2f}.')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoa in galera:
    if pessoa['sexo'] in 'F':
        print(f'({pessoa["nome"]}) ', end='')
print()
print('D) Lista de pessoas acima da média: ')
for pessoa in galera:
    if pessoa['idade'] >= media:
        print('   ', end='')
        for chave, valor in pessoa.items():
            print(f'{chave} = {valor}; ', end='')
        print()
print('<< ENCERADO >>')

