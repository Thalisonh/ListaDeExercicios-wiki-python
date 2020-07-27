'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
'''

class Macaco:
    def __init__(self, nome):
        self.__nome = nome
        self.__estomago = ""

        def comendo(self, comida):
            self.__estomago = comida

        def ver_bucho(self):
            return self.__estomago

        def digerir(self):
            self.__estomago.clear()

macaco1 = Macaco("Thalison")
macaco2 = Macaco("Henrique")

for i in range(3):
    comida = input("Digite a comida: ")
    macaco1.comendo(comida)
