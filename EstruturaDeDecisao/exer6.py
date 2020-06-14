'''Faça um Programa que leia três números e mostre o maior deles.'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

if numero3 > maior:
    maior = numero3

print(maior)