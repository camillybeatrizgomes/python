from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precoFormatado = f"{self.preco:,.2f}"
        conteudo += f"{precoFormatado.center(30, '.')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)  
        print(etiqueta)

p1 = Produto("Celular Samsung", 1_200.23)
p1.etiqueta()

p2 = Produto("Notebook Gamer", 8_000)
p2.etiqueta()