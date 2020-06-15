'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.'''

numero = float(input("Digite um número: "))

if (numero * 10) == (round(numero) * 10):
    print("Número inteiro")
else:
    print("Número decimal")



