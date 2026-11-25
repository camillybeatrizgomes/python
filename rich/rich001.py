# Importa a função print da biblioteca rich, que permite impressão colorida e com emojis no terminal. Para usar a biblioteca rich, certifique-se de instalá-la usando o comando: pip install rich
from rich import print

# Imprime a mensagem "Olá, Mundo!" em azul, junto com o emoji da Terra
print('Olá, [blue]Mundo[/blue]! :earth_americas:')
# Imprime a mensagem "Olá, Pequeno Gafanhoto" em negrito, vermelho com fundo verde, junto com o emoji de saudação vulcana
print('Olá, [bold red on green]Pequeno Gafanhoto[/] :vulcan_salute:')
# Para buscar mais emojis, basta usar o comando: python -m rich.emoji
# O comando acima abrirá uma lista de emojis disponíveis na biblioteca rich, permitindo que você escolha e utilize os emojis desejados em suas mensagens.
