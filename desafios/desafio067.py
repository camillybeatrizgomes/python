contador = 0
while True:
    n = int(input('Quer a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 20)
    for contador in range(1, 11):
        print(f'{n} x {contador} = {n * contador}')
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre! ')
