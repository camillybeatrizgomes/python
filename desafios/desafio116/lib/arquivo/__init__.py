def arquivoExiste(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo!')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso!')


def lerArquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
