'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos para o local.
'''

#inicia a classe retangulo
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    #metodo muda os valores
    def mudar_valor_lados(self):
        self.comprimento = float(input("Digite o novo valor do comprimento: "))
        self.largura = float(input("Digite o novo valor da largura: "))

    #mostra os valores ao usuario
    def retorna_valor(self):
        return self.comprimento, self.largura

    #calcula area
    def area(self):
        area = self.comprimento * self.largura
        return area

    #calcula perimetro
    def perimetro(self):
        perimetro = 2 * (self.comprimento + self.largura)
        return perimetro

print("Digite as medidas do local.")
#pede os dados inicias ao usuario
comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))

#chama a classe
retungulo = Retangulo(comprimento, largura)

#muda e mostra os valores ao usuario
mudar_valor = retungulo.mudar_valor_lados()
mostrar_valores = retungulo.retorna_valor()
print("Comprimento: {} Largura: {}".format(mostrar_valores[0], mostrar_valores[1]))

#pede e calcula a quantidad de piso e rodape
pisos = float(input("Digite a area dos pisos: "))
quantidade_pisos = retungulo.area() / pisos
total = (quantidade_pisos * 0.10) + quantidade_pisos
print("O número de pisos necessário é {} unds.".format(int(quantidade_pisos)))



