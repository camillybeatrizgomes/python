from rich.panel import Panel
from rich import print

class Churrasco:
    # Atributos de Classe
    precoDaCarne:float = 82.40 # Cada Kg de carne custa R$ 82.40
    consumoPadrao:float = 0.400 # Cada pessoa come em média 400g de carne 

    def __init__(self, titulo, quantidade):
        # Atributos de Instância
        self.titulo = titulo
        self.quantidade = quantidade

    def calculoDeQuantidadeDeCarne(self) -> float:
        return self.quantidade * Churrasco.consumoPadrao
    
    def calculoDoPrecoTotal(self) -> float:
        return self.precoDaCarne * self.calculoDeQuantidadeDeCarne()
    
    def calculoDoPrecoPorPessoa(self) -> float:
        return self.calculoDoPrecoTotal() / self.quantidade
    
    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/]\n"
        conteudo += f"Cada participante comerá {Churrasco.consumoPadrao}Kg e cada Kg custa R$ {Churrasco.precoDaCarne:,.2f}\n"
        conteudo += f"Recomendo [blue]comprar {self.calculoDeQuantidadeDeCarne():.3f}Kg[/] de carne\n"
        conteudo += f"O custo total será de [green]R$ {self.calculoDoPrecoTotal():,.2f}[/]\n"
        conteudo += f"Cada pessoa pagará [yellow]R$ {self.calculoDoPrecoPorPessoa()}[/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

c2 = Churrasco("Festa de fim de ano", 80)
c2.analisar()