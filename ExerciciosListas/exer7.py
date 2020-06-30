'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''

numero = []
soma = 0
multiplicacao = 1

for i in range(5):
    n = int(input("Digite um número: "))
    soma = soma + n
    multiplicacao = multiplicacao * n
    numero.append(n)

print()
print(f'Números: {numero}')
print(f'Soma: {soma}')
print(f'Multiplicação: {multiplicacao}')