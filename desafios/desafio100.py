from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for contador in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.4)
    print('PRONT0!')


def somarPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somarPar(numeros)