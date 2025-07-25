from time import sleep
cores = ('\033[m',  # 0 - Sem cor
         '\033[0;30;41m',  # 1 - Vermelho
         '\033[0;30;42m',  # 2 - Verde
         '\033[0;30;43m',  # 3 - Amarelo
         '\033[0;30;44m',  # 4 - Azul
         '\033[0;30;45m',  # 5 - Roxo
         '\033[7;30;97m'  # 6 - Branco
         )


def ajuda(c):
    titulo(f'Acessando o manual do comando \'{c}\'', 4)
    print(cores[6], end='')
    help(c)
    print(cores[0], end='')
    sleep(2)


def titulo(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)
    print(cores[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)