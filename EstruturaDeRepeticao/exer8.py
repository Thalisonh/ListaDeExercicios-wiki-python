'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

n = 0
soma = 0
media = 0
while(n < 5):
    numero = int(input("Digite um número: "))
    soma = soma + numero
    n += 1

media = soma / n

print(f'A soma: {soma}')
print(f'A média: {media}')