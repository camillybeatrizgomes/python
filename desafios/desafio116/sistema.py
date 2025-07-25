from desafio116.lib.interface import *
from desafio116.lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
