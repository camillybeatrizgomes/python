lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são imutáveis
# lanche[1] = 'Refrigerante'
# print(lanche) COMANDO ERRADO

# print(lanche[2])
# print(lanche[1:3])
# print(lanche[:2])
# print(lanche[-2])

# ---------------------------------------------
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')

# ---------------------------------------------
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')
# print('Comi pra caramba!')

# ---------------------------------------------
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!')

# ---------------------------------------------
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# print(sorted(lanche))

# ---------------------------------------------
# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c)
# print(len(c))
# print(c.count(5))
# print(c.index(8))
# print(c.index(2, 1))

# ---------------------------------------------
pessoa = ('Camilly', 21, 'F', 83.34)
del(pessoa)
print(pessoa)