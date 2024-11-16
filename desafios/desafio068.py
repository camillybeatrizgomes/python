from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)
vitorias = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo != 'P' and tipo != 'I':
        tipo = str(input('Par ou Ímpar: [P / I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total foi {total}. ',end='')
    print('DEU PAR! ' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu! ')
            vitorias += 1
        else:
            print('Você perdeu! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! ')
            vitorias += 1
        else:
            print('Você perdeu! ')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você teve {vitorias} vitórias')
