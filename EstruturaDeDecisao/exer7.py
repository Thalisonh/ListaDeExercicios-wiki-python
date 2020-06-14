'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

if numero3 > maior:
    maior = numero3

elif numero3 < menor:
    menor = numero3

print(f'Maior: {maior}, Menor: {menor}')