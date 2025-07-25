def aumentar(preco=0, taxa=0, formatar=False):
    """
    Aumenta o preço com uma determinada taxa.
    :param preco: Preço a ser aumentado
    :param taxa: Taxa de aumento
    :param formatar: Se True, formata o preço para moeda
    :return: Preço aumentado
    """
    resultado = preco + (preco * taxa / 100)
    return resultado if not formatar else formatar_moeda(resultado)


def diminuir(preco=0, taxa=0, formatar=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if not formatar else formatar_moeda(resultado)


def dobro(preco=0, formatar=False):
    resultado = preco * 2
    return resultado if not formatar else formatar_moeda(resultado)


def metade(preco=0, formatar=False):
    resultado = preco / 2
    return resultado if not formatar else formatar_moeda(resultado)


def formatar_moeda(preco=0, simbolo='R$'):
    return f'{simbolo} {preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{formatar_moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}')
    print(f'{taxa_reducao}% de redução: \t{diminuir(preco, taxa_reducao, True)}')
    print('-' * 30)
