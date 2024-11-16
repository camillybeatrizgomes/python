frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inversao = juntar[::-1]
print('O inverso de {} é {}'.format(juntar, inversao))
if juntar == inversao:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
