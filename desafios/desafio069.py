pessoasMaior = homens = mulheresMenor = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M / F]: ')).strip().upper()[0]
        if idade > 18:
            pessoasMaior += 1
        if sexo == 'M':
            homens += 1
        if mulheresMenor < 20:
            mulheresMenor += 1
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S / N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {pessoasMaior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresMenor} mulheres com menos de 20 anos')
