'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

quantidade = int(input("Digite a quantidade de números: "))

soma = 0
n = 0
maior = 0
menor = 0

while n < quantidade:  
    numeros = int(input("Digite um número: "))
    if n == 0:
        maior = numeros
        menor = numeros
        soma = soma + numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros <  menor:
            menor = numeros
        soma = soma + numeros
    n += 1

print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Soma: {soma}')
