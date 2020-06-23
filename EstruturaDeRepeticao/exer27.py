'''Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''

n = 0 
media = 0
soma = 0

quantidade_turmas = int(input("Digite a quantidade de turmas: "))
while n < quantidade_turmas:
    alunos_turma = int(input("Digite a quantidade de alunos turma: "))
    if alunos_turma > 40:
        alunos_turma = int(input("Digite uma nova quantidade: "))
    soma = soma + alunos_turma
    n += 1

media = soma / quantidade_turmas
print(f'O número médio de alunos por turma é de {media}')
