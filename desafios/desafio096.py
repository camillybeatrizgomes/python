print('{:^30}'.format('Controle de Terrenos'))
print('-' * 30)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))


def area():
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {a} m².')


area()