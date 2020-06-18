'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

numero = int(input("Digite um numero: "))

n = 1
flag = 0
while n < numero:
    if numero % n == 0:
        flag += 1
        n += 1
    else:
        n += 1

if flag == 1:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')

print(numero)