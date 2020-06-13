'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = float(input("Quanto você ganha por hora?: "))

horas_trabalhadas = float(input("Número de horas trabalhadas?: "))

salario = valor_hora * horas_trabalhadas

print('O salário é de R${:.2f}'.format(salario))