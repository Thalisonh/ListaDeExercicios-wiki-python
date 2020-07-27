'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''

class Tv:
    #atributos
    def __init__(self, canal, volume):
        self.__canal = canal
        self.__volume = volume

    #metodos
    def aumentar_volume(self, volume):
        self.__volume += volume

    def diminuir_volume(self, volume):
        self.__volume -= volume

    def trocar_canal(self, canal):
        self.__canal = canal

    def status(self):
        print("Canal: {}".format(self.__canal))
        print("Volume: {}".format(self.__volume))

canal = int(input("Digite o número do canal: "))

print("Volume de 0 à 10:")
volume = int(input("Digite o volume inicial: "))

tv = Tv(canal, volume)

aumentar_volume = int(input("Aumentar volume em: "))
tv.aumentar_volume(aumentar_volume)

diminuir_volume = int(input("Diminuir volume em: "))
tv.diminuir_volume(diminuir_volume)

mudar_canal = int(input("Digite um novo canal: "))
tv.trocar_canal(mudar_canal)

tv.status()

