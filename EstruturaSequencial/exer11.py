'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

A - o produto do dobro do primeiro com metade do segundo .

B - a soma do triplo do primeiro com o terceiro.

C - o terceiro elevado ao cubo.'''

num1 = int(input("Digite um número inteiro: "))

num2 = int(input("Digite outro número inteiro: "))

num3 = float(input("Digite um número real: "))

a = (num1 * num1) * (num2 / 2)

b = (3 * num1) + num3

c = num3 ** 3

print(f'Resultado de A: {a}')
print(f'Resultado de B: {b}')
print(f'Resultado de C: {c}')
