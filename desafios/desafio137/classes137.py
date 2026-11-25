from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome:str, extensao:str, tamanho:int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = extensao

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, extensao:str):
        formatos = ["pdf", "docx", "psd"]
        extensao = extensao.lower().strip()
        if extensao in formatos:
            self._extensao = extensao
        else:
            raise AttributeError("O arquivo está em um formato não suportado.")

    @property
    def nomeCompleto(self):
        return f"'{self.nome}.{self.extensao}' ({self.tamanho/1_000_000}MB)"

    @abstractmethod
    def abrir(self):
        pass

class DOC(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, "docx", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nomeCompleto} no Microsft Word.")

class PDF(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, "pdf", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nomeCompleto} no Adobe Reader.")

# Novo desafio
class PSD(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, "psd", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nomeCompleto} no Photoshop.")

def abrirArquivo(arquivo):
    arquivo.abrir()