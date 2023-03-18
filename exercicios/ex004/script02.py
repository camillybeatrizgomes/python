n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2 
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {},\n a subtração é {},\n o produto é {}\n e a divisão é {:.3f}'.format(s, sub, m, d), end=' ') 
# Na divisão, o .3f significa que o resultado terá no máximo 3 casas decimais.
# O parametro end significa não quebrar linha de um print pro outro, podendo adicionar algum caractere.
print('A divisão inteira é {} e a potência é {}'.format(di, e))

