#print('\033[7;97m Olá, Mundo!\033[m')
# a = 3
# b = 5
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

# -------------------------------------

# nome = 'Camilly'
# cores = {'limpa':'\033[m',
#          'azul':'\033[34m',
#          'amarelo':'\033[33m',
#          'pretobranco':'\033[7;97m'}
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretobranco'], nome, cores['limpa']))

# --------------------------------------

nome = 'Camilly'
cores = {'preto':'\033[1;30;41m', # Estilo da fonte: Negrito, Fonte: preto, Fundo: vermelho
        'vermelho':'\033[4;31;40m', # Estilo da fonte: sublinhado, Fonte: vermelho, Fundo: preto
        'verde':'\033[7;32;43m', # Estilo da fonte: reverter cor de fonte com o de fundo, Fonte: verde, Fundo: amarelo
        'amarelo': '\033[4;33;42m', # Estilo da fonte: sublinhado, Fonte: amarelo, Fundo: verde
        'azul': '\033[1;34;45m', # Estilo da fonte: Negrito, Fonte: azul, Fundo: roxo
        'roxo': '\033[0;35;44m',  # Estilo da fonte: nenhum, Fonte: roxo, Fundo: azul
        'ciano': '\033[7;36;107m', # Estilo da fonte: Reverter, Fonte: branco, Fundo: ciano
        'limpo': '\033[m',
        'branco': '\033[0;97;45m' # Estilo da fonte: nenhum, Fonte: branco, Fundo: roxo
}
print('{}{}!!!{}'.format(cores['verde'], nome, cores['limpo']))