from hashlib import sha256

class ContaBancaria:
    """
        Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id # protegido (#)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        if chave is None:
            chave = self.pedeSenha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f"Conta {self._id} criada com sucesso!\nSaldo atual de R$ {self.__saldo:,.2f}")

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def pedeSenha(self) -> str:
        from pwinput import pwinput
        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
        return senha

    def validarSenha(self, chave:str) -> bool:
        if chave is None:
            return False
        usuario = sha256(chave.encode()).hexdigest()
        return usuario == self.__hash

    def depositar(self, valor):
        # abs() garante que o valor seja positivo, mesmo que o usuário tente sacar um valor negativo.
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R$ {valor:,.2f} autorizado na conta {self._id}")

    def sacar(self, valor:float, chave:str =None):
        valor = abs(valor)
        if chave is None:
            chave = self.pedeSenha()
        if self.validarSenha(chave):
            if valor > self.__saldo:
                print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE!")
            else:
                self.__saldo -= valor
                print(f"Saque de R$ {valor:,.2f} autorizado na conta {self._id}")
        else:
            print("Senha não confere. Saque não autorizado!")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novoNome:str = None):
        chave = self.pedeSenha()
        if self.validarSenha(chave):
            if len(novoNome) >= 5:
                self._titular = novoNome
        else:
            print("Senha não confere. Não é possível alterar o nome!")

