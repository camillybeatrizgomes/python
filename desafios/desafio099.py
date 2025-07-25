from time import sleep


def maior(* numeros):
    maior = contador = 0
    print('=' * 40)
    print('Analisando os valores passados...')
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 1)
