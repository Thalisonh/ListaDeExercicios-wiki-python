'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

numero = []
inverso = []

for i in range(10):
    numero.append(int(input("Digite um número: ")))

n = 9
while n >= 0:
    inverso.append(numero[n])
    n -= 1

print()
print(inverso)