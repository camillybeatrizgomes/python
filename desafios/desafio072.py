numeros = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete',
           'Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze',
           'Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
valor = int(input('Digite um número entre 0 a 20: '))
while valor > 20:
    valor = int(input('Tente novamente. Digite um número entre 0 a 20: '))
print(f'Você digitou o número {numeros[valor]}')