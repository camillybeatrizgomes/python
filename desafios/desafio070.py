print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
total = produtoBarato = produtoAcimaDeMil = cont = 0
nomeProdutoBarato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    total += preço
    cont += 1
    if preço > 1000:
        produtoAcimaDeMil += 1
    if cont == 1 or preço < produtoBarato:
        nomeProdutoBarato = produto
        produtoBarato = preço
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [N / S] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 30)
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {produtoAcimaDeMil} produtos custando mais de R$ 1.000')
print(f'O produto mais barato foi {nomeProdutoBarato} que custa R$ {produtoBarato:.2f}')