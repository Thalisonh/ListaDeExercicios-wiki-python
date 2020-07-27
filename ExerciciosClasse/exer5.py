'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''

class Conta:
    #atributos 
    def __init__(self, numero, titular):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0

    #metodos
    def alterarNome(self, nome):
        self.__titular = nome
    
    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print("Numero da conta: {}".format(self.__numero))
        print("Titular: {}".format(self.__titular))
        print("Saldo: {}".format(self.__saldo))

#entrada de dados
numero = input("Digite o número da conta: ")
titular = input("Nome do titular: ")

#inicialização do objeto
conta = Conta(numero, titular)

deposito = float(input("Digite o valor do deposito: "))
conta.deposito(deposito)

saque = float(input("Digite o valor do saque: "))
conta.saque(saque)

conta.extrato()

novo_nome = input("Digite o novo nome: ")
conta.alterarNome(novo_nome)

conta.extrato()

    
        