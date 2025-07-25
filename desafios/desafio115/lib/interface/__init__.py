def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferia não digitar essa número.\033[m')
            return 0
        else:
            return numero


def linha(tamanho=35):
    return '-' * tamanho


def cabeçalho(texto):
    print(linha())
    print(texto.center(35))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[0;33m{contador}\033[m - \033[0;34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('Sua opção: ')
    return opcao
