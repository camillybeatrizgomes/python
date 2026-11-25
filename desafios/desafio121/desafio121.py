from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.paginaAtual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]'{self.titulo}'[/red] que tem [green]{self.paginas} páginas[/green] no total. Você agora está na [yellow]página {self.paginaAtual}[/yellow][/]")

    def avancarPaginas(self, quantidadeDePaginas = 1):
        contador = 0
        for paginas in range(0, quantidadeDePaginas, 1):
            if not self.fimDoLivro():
                self.paginaAtual += 1
                print(f"Pág{self.paginaAtual} :arrow_forward: ", end="")
                sleep(0.5)
                contador += 1
        print(f"[blue]Você avançou {contador} páginas e agora está na [yellow]página {self.paginaAtual}[/yellow][/]")
        if self.fimDoLivro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/red]")

    def fimDoLivro(self):
        if self.paginaAtual == self.paginas:
            return True
        else:
            return False

l1 = Livro("10 coisas que aprendi", 20)
l1.avancarPaginas(10)
l1.avancarPaginas(40)