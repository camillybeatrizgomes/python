d = float(input('Quanto dinheiro você tem na carteira: R$'))
print('Com R${:.2f} você pode comprar US${:.2f} e €{:.2f}'.format(d, (d/5.28), (d/5.66)))