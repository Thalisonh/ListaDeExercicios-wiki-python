'''
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''

vetor_1 = []
vetor_2 = []
composto = []

for i in range(10):
    vetor_1.append(input("Digite um elemento: "))

for i in range(10):
    vetor_2.append(input("Digite um elemento: "))

i = 0
n = 0

while n < 10:
    composto.append(vetor_1[i])
    composto.append(vetor_2[i])
    i += 1
    n += 1

print(f'Vetor 1: {vetor_1}')
print(f'Vetor 2: {vetor_2}')
print(f'Composto: {composto}')