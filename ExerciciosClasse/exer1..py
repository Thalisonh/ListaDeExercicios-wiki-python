'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self, cor, circunferencia, material):
        #Atributos: Cor, circunferência, material
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    #metodos
    def troca_cor(self):
        nova_cor = input("Digite um nova cor: ")
        self.cor = nova_cor

    def mostra_cor(self):
        print("A nova cor é: {}".format(self.cor))

#entrada do usuario
print("Digite os atributos da bola")
cor = input("Cor: ")
circunferencia = float(input("Circunferência: "))
material = input("Material: ")

#usando a classe
bola = Bola(cor, circunferencia, material)
troca_cor = bola.troca_cor()
motra_cor = bola.mostra_cor()
