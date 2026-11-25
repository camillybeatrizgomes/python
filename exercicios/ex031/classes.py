class Carteira:
    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R$ {self.saldo:,.2f} na carteira"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Você não tem autorização para alterar o saldo desse jeitos")

    def __eq__(self, outro):
        if self.saldo == outro.saldo:
            return True
        else:
            return False

    def __iadd__(self, valor: int|float):
        self.__saldo += valor
        return self

    def __isub__(self, valor: int|float):
        self.__saldo -= valor
        return self

    '''
        Métodos Mágicos para Operadores

    Os métodos mágicos são métodos especiais que permitem que você defina o comportamento de operadores para objetos da sua classe. 

    Equal to (==): O método mágico __eq__ é chamado quando você usa o operador == para comparar dois objetos. Você pode definir como a igualdade é determinada para os objetos da sua classe.

    Not equal to (!=): O método mágico __ne__ é chamado quando você usa o operador != para comparar dois objetos. Você pode definir como a desigualdade é determinada para os objetos da sua classe.

    Less than (<): O método mágico __lt__ é chamado quando você usa o operador < para comparar dois objetos. Você pode definir como a comparação de "menor que" é determinada para os objetos da sua classe.

    Less than or equal to (<=): O método mágico __le__ é chamado quando você usa o operador <= para comparar dois objetos. Você pode definir como a comparação de "menor ou igual a" é determinada para os objetos da sua classe.

    Greater than (>): O método mágico __gt__ é chamado quando você usa o operador > para comparar dois objetos. Você pode definir como a comparação de "maior que" é determinada para os objetos da sua classe.

    Greater than or equal to (>=): O método mágico __ge__ é chamado quando você usa o operador >= para comparar dois objetos. Você pode definir como a comparação de "maior ou igual a" é determinada para os objetos da sua classe.

    In-place addition (+=): O método mágico __iadd__ é chamado quando você usa o operador += para adicionar um valor a um objeto. Você pode definir como a adição é realizada para os objetos da sua classe.

    In-place subtraction (-=): O método mágico __isub__ é chamado quando você usa o operador -= para subtrair um valor de um objeto. Você pode definir como a subtração é realizada para os objetos da sua classe.
    '''