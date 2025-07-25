lista = list()
# Inicializa uma lista vazia para armazenar os valores.

for cont in range(0, 5):
    # Um loop que será executado 5 vezes (de 0 a 4).

    n = int(input('Digite um valor: '))
    # Solicita ao usuário que digite um valor inteiro.

    if cont == 0 or n > lista[-1]:
        # Verifica se é o primeiro número ou se o número é maior que o último elemento da lista.
        lista.append(n)
        # Adiciona o número ao final da lista.
        print('Adicionando ao final da lista...')
    else:
        indice = 0
        # Inicializa um índice para procurar onde inserir o número.
        while indice < len(lista):
            # Percorre a lista até encontrar a posição adequada.
            if n <= lista[indice]:
                # Verifica se o número é menor ou igual ao elemento atual.
                lista.insert(indice, n)
                # Insere o número na posição correta.
                print(f'Adicionando na posição {indice} da lista...')
                break
                # Sai do loop, pois a posição já foi encontrada.
            indice += 1
            # Incrementa o índice para continuar a busca.

print('-=' * 25)
print(f'Os valores digitados em ordem foram: {lista}')
