'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

if numero1 > numero2:
    if numero2 > numero3:
        maior = numero1
        meio = numero2
        menor = numero3
    else:
        maior = numero1
        meio = numero3
        menor = numero2

if numero2 > numero1:
    if numero1 > numero3:
        maior = numero2
        meio = numero1
        menor = numero3
    else:
        maior = numero2
        meio = numero3
        menor = numero1

if numero3 > numero1:
    if numero1 > numero2:
        maior = numero3
        meio = numero1
        menor = numero2
    else:
        maior = numero3
        meio = numero2
        menor = numero1

print(f'Maior: {maior}')
print(f'Meio: {meio}')
print(f'Menor: {menor}')
