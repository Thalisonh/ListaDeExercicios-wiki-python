'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

quantidade = int(input("Digite a quantidade de números: "))

soma = 0
n = 0
maior = 0
menor = 0

while n < quantidade:  
    numeros = int(input("Digite um número: "))
    if numeros < 0 or numeros > 1000:
        numeros = int(input("Digite um novo número: "))
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