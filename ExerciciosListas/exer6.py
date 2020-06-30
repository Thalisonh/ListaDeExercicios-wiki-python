'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''

alunos = []
nota = 0
media = 0
soma = 0
maior = 0

for i in range(3):
    for j in range(4):
        nota = float(input("Digite a nota: "))
        soma = soma + nota

    media = soma / 4
    if media >= 7:
        maior += 1

    alunos.append(media)

    media = 0
    soma = 0

print(f'Média dos alunos: {alunos}')
print(f'Quantidade de médias maiores ou igual á 7: {maior}')