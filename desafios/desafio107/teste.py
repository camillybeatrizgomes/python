import moeda

preco = float(input('Digite um preço: R$ '))

print(f'A metade de R$ {preco:.2f} é R$ {moeda.metade(preco):.2f}')
print(f'O dobro de R$ {preco:.2f} é R$ {moeda.dobro(preco):.2f}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preco, 10):.2f}')
