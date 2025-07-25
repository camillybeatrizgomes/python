def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero


def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número real válido.\033[m')
            continue # Esse comando faz o loop voltar ao início
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
