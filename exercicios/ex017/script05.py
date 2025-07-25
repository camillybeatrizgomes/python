def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [6, 3, 9, 1, 8, 2]
dobra(valores)
print(valores)