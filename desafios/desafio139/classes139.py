from rich import print
from rich.panel import Panel

class Mensagem:
    def __init__(self, mensagem:str = "", tipo:str = "aviso", icone:str = ":speech_balloon:"):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        mensagem = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", style="#ffffff on #000000", width=50)
        print(mensagem)

class Alerta(Mensagem):
    def __init__(self, mensagem:str = ""):
        super().__init__(mensagem, tipo = "alerta", icone = ":warning:")

    def mostrar(self):
        mensagem = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", style="#000000 on #fffc1b", width=50)
        print(mensagem)


class Erro(Mensagem):
    def __init__(self, mensagem:str = ""):
        super().__init__(mensagem, tipo = "erro", icone = ":prohibited:")

    def mostrar(self):
        mensagem = Panel(self._mensagem, title=f"{self._icone} {self._tipo.upper()} {self._icone}", style="#ffff00 on #880000", width=50)
        print(mensagem)
