from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()
    
    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)
    
    def ficha(self):
        conteudo = f"Nome real: [black on white]{self.nome}[/]"
        conteudo += "\nJogos Favoritos: "
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        ficha = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(ficha)


j1 = Gamer("Camilly Beatriz", "HiddenPlayz")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("EA Football")
j1.ficha()