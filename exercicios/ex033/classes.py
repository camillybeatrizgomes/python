class Numero:
    def __init__(self, valor:int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do Número"

class Texto:
    def __init__(self, txt: str = ""):
        self.texto = txt

    def dobrar(self):
        self.texto = self.texto + " " + self.texto

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do Texto"

class Lista:
    def __init__(self, lista: list = []):
        self.lista = lista

    def dobrar(self):
        self.lista = self.lista + self.lista

    def __str__(self):
        return f"Tenho os itens {self.lista} dentro da Lista"

class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f"O papel está {"novo" if not self.dobrado else "dobrado"}"

class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa, muito engraçada..."

# DUCK TYPING 
def tentarDobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Tive dificuldades para dobrar {objeto.__class__.__name__}")