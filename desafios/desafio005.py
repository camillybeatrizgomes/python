a = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é',type(a))
print('Só tem espaços? ',a.isspace())  # Verifica se tem somente espaços
print('É um número? ',a.isnumeric())  # Verifica se é um número
print('É alfabético? ',a.isalpha())  # Verifica se é letra
print('É alfanumérico? ',a.isalnum())  # Verifica se é letra ou número
print('Está em maiúsculas? ',a.isupper()) # Verifica se é composto por letras maiúsculas
print('Está em minúsculas? ',a.islower()) # Verifica se é composto por letras minúsculas
print('Está capitalizada? ',a.istitle())  # Verifica em texto começam com uma letra maiúscula
