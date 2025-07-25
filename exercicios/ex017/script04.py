def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')


contador(2, 1, 4)
contador(2, 8)
contador(4, 4, 7, 6, 2)