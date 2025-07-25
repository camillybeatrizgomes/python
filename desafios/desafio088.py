from random import randint
from time import sleep
lista = list()
jogos = list()
total = 1
print('-=' * 25)
print('{:^50}'.format('JOGA NA MEGA SENA'))
print('-=' * 25)
quantidade = int(input('Quantos jogos quer que eu sorteie? '))
while total <= quantidade:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '-=' * 3)
for indice, lista in enumerate(jogos):
    print(f'JOGO {indice + 1}: {lista}')
    sleep(1)
print('=-' * 5, '< BOA SORTE >', '-=' * 5)

