from desafio117.lib.arquivo import *
from desafio117.lib.interface import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
