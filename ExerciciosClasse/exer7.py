'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

a. Atributos: Nome, Fome, Saúde e Idade 
b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
'''

class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.__nome = nome
        self.__fome = fome
        self.__saude = saude
        self.__idade = idade

    def alterar_nome(self, nome):
        self.__nome = nome

    def alterar_fome(self):
        if self.__fome == True:
            self.__fome = False
        else:
            self.__fome = True

    def alterar_saude(self, saude):
        self.__saude = saude

    def alterar_idade(self, idade):
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_fome(self):
        return self.__fome

    def get_saude(self):
        return self.__saude

    def get_idade(self):
        return self.__idade

nome = input("Digite o nome do bichinho: ")

fome = input("Digite se ele está com fome: ")
if fome.upper == "SIM":
    fome = True
else:
    fome = False

idade = int(input("Digite a idade: "))

saude = input("Digite a saúde do bichinho: ")

bichinho = Bichinho(nome, fome, saude, idade)

print(bichinho.get_nome())
print(bichinho.get_fome())
print(bichinho.get_saude())
print(bichinho.get_idade())

bichinho.alterar_nome("Thalison")
bichinho.alterar_fome()
bichinho.alterar_saude("Pessima")
bichinho.alterar_idade(18)
print()

print(bichinho.get_nome())
print(bichinho.get_fome())
print(bichinho.get_saude())
print(bichinho.get_idade())
