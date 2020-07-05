"""
Escreva um programa de bancos que possua:
    Uma classe Banco com os atributos
    - private total
    - public TaxaReserva
    - private reservaExigida

    E métodos
    - public podeFazerEmprestimo(valor) --> bool
    - public MudaTotal(valor)

E uma classe conta com os atributos
    - private saldo
    - private ID
    - private senha

    E métodos
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public podeReceberEmprestimo(valor) --> bool
    - public saldo --> float
"""

class banco(object):
    __total = 10000
    TaxaReserva = 0.1
    __reservaExigida = __total * TaxaReserva
    def podeFazerEmprestimo(valor):
        if banco.__total - valor >= banco.__reservaExigida:
            banco.__total -= valor
            print('Pode receber o emprestimo')
            return True
        else:
            print('Não pode receber o empresto')
            return False
    def MudaTotal(valor):
        banco.__total += valor

class conta(object):
    def __init__(self, saldo, ID, senha):
        self.__saldo = saldo
        self.__ID = ID
        self.__senha = senha
    def deposito(self, senha, valor):
        if senha == self.__senha:
            self.__saldo += valor
            banco.MudaTotal(valor)
    def saque(self, senha, valor):
        if senha == self.__senha:
            self.__saldo -= valor
            banco.MudaTotal(-valor)
    def podeReceberEmprestimo(self, valor):
        return banco.podeFazerEmprestimo(valor)
    def saldo(self):
        print(self.__saldo)

p = conta(1000, 123, 123)
p.deposito(222, 5000)
p.saldo()
p.deposito(123, 5000)
p.saldo()
p.saque(222, 5000)
p.saldo()
p.saque(123, 5000)
p.saldo()
p.podeReceberEmprestimo(10000)
p.podeReceberEmprestimo(1000)
