def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" não é um preço válido\033[m')
        else:
            valido = True
            return float(entrada)
