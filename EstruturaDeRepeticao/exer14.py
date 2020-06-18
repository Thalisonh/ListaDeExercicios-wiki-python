'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''

n = 0
par = 0
impar = 0

while(n < 10):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    n += 1

print(f'Pares: {par}')
print(f'Impares: {impar}')
