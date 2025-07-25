teste = list()
teste.append('Camilly')
teste.append(21)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

print(galera)