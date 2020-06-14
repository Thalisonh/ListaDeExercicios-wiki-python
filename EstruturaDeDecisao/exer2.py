'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

numero = int(input("Digite um número: "))

if numero > 0:
    print("Número positivo!")
elif numero < 0:
    print("Número negativo!")
else:
    print("O número é 0!")