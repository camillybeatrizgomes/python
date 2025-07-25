from desafio115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        print('Opção 01')
    elif resposta == 2:
        print('Opção 02')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0;31mERRO: Digite uma opção válida.\033[m')
    sleep(2)
