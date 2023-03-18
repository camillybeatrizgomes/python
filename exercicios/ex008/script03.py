nome = 'Camilly'
cores = {'preto':'\033[1;30;41m', # Estilo da fonte: Negrito, Fonte: preto, Fundo: vermelho
        'vermelho':'\033[4;31;40m', # Estilo da fonte: sublinhado, Fonte: vermelho, Fundo: preto
        'verde':'\033[7;32;43m', # Estilo da fonte: reverter cor de fonte com o de fundo, Fonte: amarela, Fundo: verde
        'amarelo': '\033[4;33;42m', # Estilo da fonte: sublinhado, Fonte: amarelo, Fundo: verde
        'azul': '\033[1;34;45m', # Estilo da fonte: Negrito, Fonte: azul, Fundo: roxo
        'roxo': '\033[0;35;44m',  # Estilo da fonte: nenhum, Fonte: roxo, Fundo: azul
        'ciano': '\033[7;36;107m', # Estilo da fonte: Reverter, Fonte: branco, Fundo: ciano
        'limpo': '\033[m',
        'branco': '\033[0;97;45m' # Estilo da fonte: nenhum, Fonte: branco, Fundo: roxo
}
print('{}{}!!!{}'.format(cores['branco'], nome, cores['limpo']))



