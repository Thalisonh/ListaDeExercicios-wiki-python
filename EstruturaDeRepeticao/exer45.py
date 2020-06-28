'''Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
'''

gabarito = ["A","B","C","D","E","E","D","C","B","A"]
nota = []
acertos = 0

n = 1
quantidade_alunos = int(input("Digite a quantidade de alunos: "))
print()

while n <= quantidade_alunos:

    print(f'Digite o gabarito do aluno {n}')
    print()

    for i in range(10):
        nota.append(input("Digite a respota da alternativa {}: ".format(i + 1)))
        if nota[i] == gabarito[i]:
            acertos += 1
    print()
    print(f'Aluno {n} teve {acertos} acertos.')
    print()

    acertos = 0
    nota.clear()
    n += 1

