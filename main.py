from validador_de_cpf import validador_cpf
from validador_de_cnpj import validador_cnpj


class Empresa:

    def __init__(self, cnpj: str, taxa: int | float, saldo: int | float = 1000):

        self.cnpj = cnpj
        self.taxa = taxa
        self.saldo = saldo

    def saque(self, valor):
        if validador_cnpj(self.cnpj):
            if valor < self.saldo:
                porcentagem_taxa = self.taxa / 100
                valor_taxa = valor * porcentagem_taxa
                _saque = valor - valor_taxa
                self.saldo -= _saque
                print(f'Você sacou {_saque}, seu saldo é: {self.saldo}')
            else:
                print('Sem saldo')
        else:
            print('Não podemos sacar com CNPJ inválido')

    def deposito(self, valor):
        porcentagem_taxa = self.taxa / 100
        valor_taxa = valor * porcentagem_taxa
        _deposito = valor - valor_taxa
        self.saldo += _deposito
        print(f'Você depositou {valor}, seu saldo é {self.saldo}')


class Cliente(Empresa):
    def __init__(self, cpf: str, taxa: int | float, cnpj: str):
        super().__init__(cnpj, taxa)
        self.cpf = cpf

    def saque(self, valor):
        if validador_cpf(self.cpf):
            super().saque(valor)
        else:
            print('Não podemos sacar com CPF inválido')

    def deposito(self, valor):
        if validador_cpf(self.cpf):
            super().deposito(valor)
        else:
            print('Não podemos depositar com CPF inválido')


e1 = Empresa('11222333000181', 5)
c1 = Cliente('48540350807', 5, '11222333000181')
c1.saque(10)
e1.deposito(41)
