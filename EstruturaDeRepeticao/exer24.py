'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

n = int(input("Digite a quantidade de notas: "))

cont = 0
soma = 0

while cont < n:
    notas = float(input("Digite uma nota: "))
    soma = soma + notas 
    cont += 1

media = soma / cont
print(f'A media das notas: {media}')