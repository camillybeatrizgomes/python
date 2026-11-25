# Importa a função print da biblioteca rich, que permite impressão colorida e com formatação especial
from rich import print
# Importa a classe Panel da biblioteca rich, usada para criar caixas/painéis estilizados no terminal
from rich.panel import Panel

# Cria um painel (caixa) com o texto centralizado e cor branca
# O painel recebe o título "Mensagem", tem borda vermelha e largura fixa de 33 caracteres
caixa = Panel(
	"[white]Esse aqui é um painel de exemplo[/]",  # Texto do painel, com cor branca
	title="Mensagem",  # Título exibido na parte superior do painel
	style="red",       # Cor da borda do painel
	width=33            # Largura do painel
)

# Exibe o painel formatado no terminal
print(caixa)