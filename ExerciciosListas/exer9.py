'''
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

numeros = []
quadrados = []
quadrado = 0

for i in range(10):
    numeros.append(int(input("Digite um número: ")))

for i in range(10):
    quadrado = numeros[i] * numeros [i]
    quadrados.append(quadrado)

print()
print(f'Números: {numeros}')
print(f'Quadrados: {quadrados}')
print(f'Soma: {sum(quadrados)}')