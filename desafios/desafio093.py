jogador = dict()
golsDasPartidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
quantidadeDePartidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for contador in range(0, quantidadeDePartidas):
    golsDasPartidas.append(int(input(f'   Quantos gols na partida {contador + 1}? ')))
jogador['gols'] = golsDasPartidas[:]
jogador['totalDeGols'] = sum(jogador["gols"])
print(jogador)
print('-=' * 25)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 25)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, valor in enumerate(jogador["gols"]):
    print(f'   => partida {indice + 1}, fez {valor} gols.')
print(f'Foi um total de {jogador["totalDeGols"]} gols.')