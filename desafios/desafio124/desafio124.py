from rich import print
from rich.panel import Panel

class ControleRemoto:
    canalMin:int = 1
    canalMax:int = 5
    volumeMin:int = 1
    volumeMax:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canalAtual:int = canal
        self.volumeAtual:int = volume
        self.ligado:bool = False

    def ligaDesliga(self):
        self.ligado = not self.ligado

    def canalMais(self):
        if self.ligado:
            if self.canalAtual == ControleRemoto.canalMax:
                self.canalAtual = ControleRemoto.canalMin
            else:
                self.canalAtual += 1

    def canalMenos(self):
        if self.ligado:
            if self.canalAtual == ControleRemoto.canalMin:
                self.canalAtual = ControleRemoto.canalMax
            else:
                self.canalAtual -= 1

    def volumeMais(self):
        if self.ligado:
            if self.volumeAtual != ControleRemoto.volumeMax:
                self.volumeAtual += 1

    def volumeMenos(self):
        if self.ligado:
            if self.volumeAtual != ControleRemoto.volumeMin:
                self.volumeAtual -= 1

    def mostrarTv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f":prohibited: [red]A TV está desligada[/]"
        else:
            conteudo = f"CANAL  = "
            for canal in range(ControleRemoto.canalMin, ControleRemoto.canalMax + 1):
                if canal == self.canalAtual:
                    conteudo += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "
            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volumeMin, ControleRemoto.volumeMax + 1):
                if volume <= self.volumeAtual:
                    conteudo += "[black on cyan] [/]"
                else:
                    conteudo += "[black on white] [/]"
        tv = Panel(conteudo, title="[ TV ]", width=30)
        print(tv)

c = ControleRemoto()
while True:
    c.mostrarTv()
    comando = str(input(f"< CH{c.canalAtual} >  - VOL{c.volumeAtual} + "))
    match comando:
        case '0':
            break
        case '@':
            c.ligaDesliga()
        case '>':
            c.canalMais()
        case '<':
            c.canalMenos()
        case '+':
            c.volumeMais()
        case '-':
            c.volumeMenos()
    print("\n" * 10)

    