'''
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
'''

idades = []
alturas = []
idade = 0
altura = 0
media_altura = 0
cont = 0

for i in range(30):
    idade = int(input("Idade: "))
    idades.append(idade)
    altura = float(input("Altura: "))
    alturas.append(altura)

media = sum(alturas) / 30

for i in range(30):
    if idades[i] > 13:
        if alturas[i] < media:
            cont += 1

print(f'Alunos maiores de 13 anos que possui altura menor que a média: {cont}')