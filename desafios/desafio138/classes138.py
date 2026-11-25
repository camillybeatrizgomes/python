from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("O pagamento só pode ser efetuado por valores positivos.")

    @property
    def valorFormatado(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True, symbol=True)

    @abstractmethod
    def pagar(valor:float):
        pass

class Boleto(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.valorFormatado} via Boleto"
        except Exception as erro:
            return f"Falha no pagamento de {self.valorFormatado} via Boleto"

class Pix(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.valorFormatado} via Pix"
        except Exception as erro:
            return f"Falha no pagamento de {self.valorFormatado} via Pix"

class CartaoDeCredito(Pagamento):
    def pagar(self, valor:float):
        try:
            self.valor = valor
            return f"Pagamento CONFIRMADO de {self.valorFormatado} via Cartão de Crédito"
        except Exception as erro:
            return f"Falha no pagamento de {self.valorFormatado} via Cartão de Crédito"

def finalizarCompra(tipo:Pagamento, valor:float):
    print(tipo.pagar(valor))