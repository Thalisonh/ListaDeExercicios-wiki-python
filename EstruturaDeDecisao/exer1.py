'''Faça um Programa que peça dois números e imprima o maior deles.'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um novo número: "))

if numero1 > numero2:
    maior = numero1
elif numero2 > numero1:
    maior = numero2

print(f'O maior número é: {maior}')