from rich import print

class Diario:
    def __init__(self, senha = "1234"):
        self.__segredos = []
        self.__senha = senha.strip()

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha!")

    @senha.setter
    def senha(self, novaSenha):
        if isinstance(novaSenha, str):
            novaSenha = novaSenha.strip()
            if len(novaSenha) >= 4:
                self.__senha = novaSenha

    def escrever(self, mensagem):
        if isinstance(mensagem, str) and len(mensagem) > 0:
            self.__segredos.append(mensagem.strip())

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler o diário!")
        else:
            print("[green]Diário LIBERADO![/]")
            for segredo in self.__segredos:
                print(f"- {segredo}")
