'''Faça um programa que leia 5 números e informe o maior número.'''

n = 1
maior = 0
while(n <= 5):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    n += 1

print(maior)