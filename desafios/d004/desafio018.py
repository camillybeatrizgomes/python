from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjante: '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))
