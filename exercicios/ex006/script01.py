frase = 'Curso em Vídeo Python'

# print(frase[3]) = s ->
# O resultado traz a terceira letra da frase, iniciando a contagem do 0.

# print(frase[0:13]) = Curso em Víde ->
# O resultado traz as letras de 0 à 13, mas a contagem irá parar no 12.

# print(frase[:13]) = Curso em Víde ->
# Será o mesmo resultado do anterior.

# print(frase[1:15:2]) = us mVdo ->
# O resultado traz as letras da frase de 1 à 15, que no caso vai até 14, pulando de 2 em 2.

# print(frase[1::2]) = us mVdoPto ->
# O resultado traz as letras da frase de 1 até a última letra, pulando de 2 em 2.

# print(frase[::2]) = Croe íe yhn ->
# O resultado traz as letras da frase da primeira até a última pulando de 2 em 2.

# print(frase.count('o')) = 3 ->
# O resultado traz quantas vezes aparece a letra 'o' na frase. OBS: se for colocado o 'o' maiúsculo, o resultado será 0.

# print(frase.upper()) = CURSO EM VÍDEO PYTHON ->
# O resultado traz a modificação das letras que estão em minúscula para maiúscula.

# print(len(frase)) = 21 ->
# O resultado traz quantos caracteres tem na frase.

# print(len(frase.strip())) = 27 ->
# Após modificado a frase com espaços desnecessários, O strip irá remove-los automaticamente.

# print(frase.replace('Python', 'Android')) = Curso em Vídeo Android ->
# O resultado traz a modificação da palavra Python para a palavra Android.

# print('Curso' in frase) = True ->
# O resultado será um valor boolean, se a frase tem a palavra Curso ou não.

# print(frase.find('V')) = 9 ->
# O resultado traz o valor da posição da letra 'v' na frase.

# print(frase.lower()) = curso em vídeo python ->
# O resultado traz a modificação das letras que estão em maiúscula para minúscula.

# print(frase.split()) = ['Curso', 'em', 'Vídeo', 'Python'] ->
# O resultado traz uma lista com as palavras da frase sentando separadas.

print('''
        Lorem ipsum dolor sit amet. Ea nihil exercitationem et rerum '
        voluptas aut sunt dignissimos et veritatis inventore in animi 
        doloremque et delectus dolor. A quisquam atque ab quibusdam 
        odit sed soluta excepturi qui sint ipsa. Et quia omnis et error
        deserunt qui reiciendis earum et molestiae nihil aut voluptates 
        dolorem sit libero nihil et delectus expedita. Ad iure consectetur
        ea omnis voluptas eum nihil atque ea quia nisi. Vel distinctio velit 
        et iste voluptatem id dolorem harum ut praesentium quae sit numquam 
        esse est voluptatum placeat eos enim harum.''')

