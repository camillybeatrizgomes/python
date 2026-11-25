# teste = list()
# teste.append('Camilly')
# teste.append(21)

# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])

# print(galera)

# ---------------------------
# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[3][1])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

# ---------------------------
galera = list()
dado = list()
totalMaior = totalMenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalMenor += 1

print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade.')
