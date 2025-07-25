from time import sleep
print('=' * 30)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = 0
        while cont <= fim:
            print(f'{cont} ',end='')
            cont += 1
            sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
            sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
print('=' * 30)
contador(10, 0,2)
print('=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
