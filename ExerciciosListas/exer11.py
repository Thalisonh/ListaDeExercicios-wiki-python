'''
Altere o programa anterior, intercalando 3 vetores de 3 elementos cada.
'''

vetor_1 = []
vetor_2 = []
vetor_3 = []
composto = []

for i in range(10):
    vetor_1.append(input("Digite um elemento: "))

for i in range(10):
    vetor_2.append(input("Digite um elemento: "))

for i in range(10):
    vetor_3.append(input("Digite um elemento: "))

i = 0
n = 0

while n < 10:
    composto.append(vetor_1[i])
    composto.append(vetor_2[i])
    composto.append(vetor_3[i])
    i += 1
    n += 1

print(f'Vetor 1: {vetor_1}')
print(f'Vetor 2: {vetor_2}')
print(f'Vetor 10: {vetor_3}')
print(f'Composto: {composto}')