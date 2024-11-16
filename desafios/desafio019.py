from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
print('O ângulo de {} tem o seno de {:.2f}'.format(a, seno))
cosseno = cos(radians(a))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(a, cosseno))
tangente = tan(radians(a))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a, tangente))
