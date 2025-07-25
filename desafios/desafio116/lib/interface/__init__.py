def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return numero


def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[0;33m{contador}\033[m - \033[0;34m{item}\033[m')
        contador += 1
    print(linha())
    opcao = leiaInt('Sua opção: ')
    return opcao
