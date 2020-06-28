'''
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
'''

numero_termos = int(input("Digite o número de termos: "))
n = 2

h = 1

for i in range(numero_termos):
    h = h + (1 / n)
    n += 1

print(h)