from desafio117.lib.interface import *

def arquivoExiste(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo!')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!')


def lerArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Houve um erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        a.close()


def cadastrarPessoa(nomeArquivo, nome='Desconhecido', idade=0):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever no arquivo!')
        else:
            print(f'Novo registro de {nome} foi adicionado.')
        finally:
            a.close()
