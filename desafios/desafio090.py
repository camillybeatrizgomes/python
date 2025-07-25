aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 7 and aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
elif aluno['media'] <= 5:
    aluno['situação'] = 'Reprovado'
print('=-' * 25)
for chave, valor in aluno.items():
    print(f'  - {chave} é igual a {valor}')