'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

A- Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;

B - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

C- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''

ano = 1995
salario_inicial = 1000
salario_final = 0
aumento = 0.015

while ano <= 2020:
    if ano == 1995:
        salario_final = salario_inicial
        print(salario_final)
    elif ano == 1996:
        salario_final = salario_inicial +  (salario_inicial / 100)
        print(salario_final)
    elif ano > 1996:
        aumento = aumento * 2
        salario_final =  salario_inicial + (salario_inicial * (aumento / 100))
        print('Salario: R${:.2f}'.format(salario_final))
    ano += 1


