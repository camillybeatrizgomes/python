def notas(*n, situacao=False):

    """
    -> Função para analisar as notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos (Pode ser várias)
    :param situacao: Indica se será exibido ou não a situação (OPCIONAL)
    :return: Retorna um dicionário com as informações sobre a situação do aluno
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resposta = notas(5.5, 7.5, 8, situacao=True)
# print(resposta)
help(notas)