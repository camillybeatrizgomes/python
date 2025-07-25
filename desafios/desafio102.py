def fatorial(valor, show=False):
    """
    -> Calcular o fatorial de um número
    :param valor: o número a ser calculado
    :param show: (Opcional) mostra ou não a conta
    :return: retorna o valor do fatorial do número (valor)
    """
    f = 1
    for contador in range(valor, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= contador
    return f


print(fatorial(5, True))
