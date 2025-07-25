valores = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado...')
    resp = str(input('Quer continuar? [S / N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 25)
valores.sort()
print(f'Você digitou os valores: {valores}')
print('-=' * 25)
