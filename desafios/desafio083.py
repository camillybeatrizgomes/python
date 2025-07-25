expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbolo)
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é errada!')
