# nome = input('Qual o seu nome? ')
# print('Prazer em te conhecer {:^20}!'.format(nome))
# Criasse um espaçamento de 20 caracteres entre o nome

# nome = input('Qual o seu nome? ')
# print('Prazer em te conhecer {:-^20}!'.format(nome))
# Criasse um traço de 20 caracteres entre o nome

# Exemplos de Operadores Aritméticos

# 5+3*2 == 11
# 19/2 == 9.5 
# 19//2 == 9   
# 365**15 == 271889832302902251378777003692626953125
# 18%3 == 0
# 15%2 == 1
# 4**2 == 16
# pow(4,2) == 16

# Ordem de Precedência 
# () (Tudo que tiver dentro dos parênteses)
# ** (Potência)
# * (Multiplicação) / (Divisão) // (Divisão inteira) % (Resto da divisão)
# + (Adição) - (Subtração) 

# ---------------------------------------

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

