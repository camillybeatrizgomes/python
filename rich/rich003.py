# Importa a função print da biblioteca rich, que permite impressão colorida e formatada
from rich import print
# Importa a classe Table da biblioteca rich, usada para criar tabelas estilizadas no terminal
from rich.table import Table

# Cria uma tabela com o título "Tabela de Preços"
tabela = Table(title="Tabela de Preços")

# Adiciona a coluna "Nome" alinhada à direita e com cor vermelha
tabela.add_column("Nome", justify="right", style="red")
# Adiciona a coluna "Preço" centralizada e com cor azul
tabela.add_column("Preço", justify="center", style="blue")
# Adiciona uma linha à tabela com os valores "Mouse" e "R$ 29.99"
tabela.add_row("Mouse", "R$ 29.99")
# Adiciona outra linha à tabela com os valores "Teclado" e "R$ 49.90"
tabela.add_row("Teclado", "R$ 49.90")

# Exibe a tabela formatada no terminal
print(tabela)
