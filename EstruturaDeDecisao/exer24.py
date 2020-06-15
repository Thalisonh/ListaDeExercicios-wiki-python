'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))

entrada = input("Digite uma operação matemática (+, -, *, /): ")

if entrada == '+':
    operacao = numero1 + numero2
elif entrada == '-':
    operacao = numero1 - numero2
elif entrada == '*':
    operacao = numero1 * numero2
elif entrada == '/':
    operacao = numero1 / numero2

if operacao % 2 == 0:
    par_ou_impar = 'Par'
else:
    par_ou_impar = 'Ímpar'

if operacao > 0:
    positivo_negativo = 'Positivo'
else:
    positivo_negativo = 'Negativo'

if (operacao * 10) == (round(operacao) * 10):
    int_float = 'Inteiro'
else:
    int_float = 'Decimal'

print(f'O resultado da operação {numero1} {entrada} {numero2} = {operacao}, o número é {par_ou_impar}, {positivo_negativo} e {int_float}')


