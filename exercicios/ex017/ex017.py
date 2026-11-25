# def linha():
#     print('-' * 30)

# linha()
# print('{:^30}'.format('CURSO EM VÍDEO'))
# linha()
# print('{:^30}'.format('APRENDER PYTHON'))
# linha()

# -------------------------------------
# def titulo(texto):
#     print('-' * 30)
#     print('{:^30}'.format(texto))
#     print('-' * 30)

# titulo('CURSO EM VÍDEO')
# titulo('PYTHON É MUITO BOM!')

# -------------------------------------
# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma vale {s}')

# soma(b = 4, a = 5)
# soma(8, 9)
# soma(a = 3, b = 1)

# -------------------------------------
# def contador(*num):
#     tamanho = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tamanho} números.')

# contador(2, 1, 4)
# contador(2, 8)
# contador(4, 4, 7, 6, 2)

# -------------------------------------
# def dobra(lista):
#     posicao = 0
#     while posicao < len(lista):
#         lista[posicao] *= 2
#         posicao += 1

# valores = [6, 3, 9, 1, 8, 2]
# dobra(valores)
# print(valores)

# -------------------------------------
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)
