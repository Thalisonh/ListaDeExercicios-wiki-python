'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    #atributo
    def __init__(self):
        self.lado = 10

    #metodos
    def mudar_valor_lado(self):
        novo_lado = int(input("Digite um novo lado: "))
        self.lado = novo_lado
        print("O novo lado do quadrado é: {}".format(self.lado))

    def area(self, area):
        self.lado = area
        resultado = self.lado * self.lado
        return resultado

#chamando o objeto
quadrado = Quadrado()
muda_valor = quadrado.mudar_valor_lado()

#entrada do usuario
valor_area = int(input("Digite o valor do lado: "))
area = quadrado.area(valor_area)
print("Área: {}".format(area))