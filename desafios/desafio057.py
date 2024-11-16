somaIdade = 0
mediaIdade = 0
maiorIdade = 0
nomeVelho = ''
totalMulher = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M / F): '))
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdade, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher))
