time = list()
jogador = dict()
golsDasPartidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    quantidadeDePartidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    golsDasPartidas.clear()
    for contador in range(0, quantidadeDePartidas):
        golsDasPartidas.append(int(input(f'   Quantos gols na partida {contador + 1}? ')))
    jogador['gols'] = golsDasPartidas[:]
    jogador['totalDeGols'] = sum(jogador["gols"])
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S / N] ')).upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERRO! digite apenas S ou N.')
    if resposta == 'N':
        break
print('-' * 55)
print('cod ', end='')
for indice in jogador.keys():
    print(f'{indice:<15}', end='')
print()
print('-' * 55)
for chave, valor in enumerate(time):
    print(f'{chave:>3} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 55)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for indice, gols in enumerate(time[busca]["gols"]):
            print(f'     No jogo {indice + 1}, fez {gols} gols.')
print('-' * 55)
print('<<< VOLTE SEMPRE >>>')
