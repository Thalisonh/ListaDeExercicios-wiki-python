'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

#instanciando o objeto Pessoa
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def envelhercer(self, envelheceu):  
        if (self.__idade <= 21):
            tempo_envelheceu = 21 - self.__idade
            self.__altura += (tempo_envelheceu * 0.5)
            self.__idade += envelheceu
        else:
            self.__idade += envelheceu

    def engordar(self, peso):
        self.__peso += peso

    def emagrecer(self, peso):
        self.__peso -= peso

    def crescer(self, altura):
        self.altura += cresceu

    def mostrar_atributos(self, nome, idade, peso, altura):
        print("Pessoa: {}".format(pessoa.__nome))
        print("Idade: {}".format(pessoa.__idade))
        print("Peso: {}".format(pessoa.__peso))
        print("Altura: {}".format(pessoa.__altura))

#entrada do usuario
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

#iniciando o objeto
pessoa = Pessoa(nome, idade, peso, altura)

idade_envelhecida = int(input("Digite o quanto envelheceu: "))
idade = pessoa.envelhercer(idade_envelhecida)

pessoa.mostrar_atributos(nome, idade, peso, altura)



