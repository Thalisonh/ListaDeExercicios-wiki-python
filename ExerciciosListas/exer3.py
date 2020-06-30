'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = []
soma = 0
media = 0

for i in range(4):
    nota = float(input("Digite sua nota: "))
    notas.append(nota)
    soma = soma + nota

media = soma / 4

print(f'Média: {media}')
