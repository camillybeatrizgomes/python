def dobro(preco, formatar=False):
    '''
    -> Calcular o dobro de um preço.
    :param preco: Preço a ser calculado.
    :param formatar: Se True, formata o resultado para moeda.
    :return: O dobro do preço.
    '''
    resultado = preco * 2
    return resultado if not formatar else moeda(resultado)


def metade(preco, formatar=False):
    resultado = preco / 2
    return resultado if not formatar else moeda(resultado)


def aumentar(preco, taxa, formatar=False):
    resultado = preco + (preco * taxa / 100)
    return resultado if not formatar else moeda(resultado)


def diminuir(preco, taxa, formatar=False):
    resultado = preco - (preco * taxa / 100)
    return resultado if not formatar else moeda(resultado)


def moeda(preco, simbolo='R$'):
    return f'{simbolo} {preco:.2f}'.replace(".", ",")
