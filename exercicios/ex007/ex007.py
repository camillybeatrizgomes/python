# nome = str(input('qual é seu nome? '))
# if nome == 'Camilly':
#     print('Que nome lindo você tem! ')
# else:
#     print('Seu nome é tão normal!!')
# print('Bom dia, {}!'.format(nome))

# --------------------------------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(media))
if media >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi baixa! Estude mais!')
