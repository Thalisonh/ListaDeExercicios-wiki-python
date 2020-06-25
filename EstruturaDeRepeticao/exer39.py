'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

numero = []
altura = []
for i in range(10):
    numero_aluno = int(input("Digite seu número: "))
    numero.append(numero_aluno)
    altura_aluno = float(input("Digite sua altura: "))
    altura.append(altura_aluno)

menor = min(altura)
maior = max(altura)

for i in range(10):
    if menor == altura[i]:
        print(f'Numero: {numero[i]}')
        print(f'Menor: {menor}')
    if maior == altura[i]:
        print(f'Numero: {numero[i]}')
        print(f'Maior: {maior}')