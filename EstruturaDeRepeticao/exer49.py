'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''

sequencia = int(input("Digite o tamanho da sequencia: "))

n = 1
m = 1
soma = 0

for i in range(sequencia):
    soma = soma + ( n / m)
    m += 2
    n += 1

print(soma)