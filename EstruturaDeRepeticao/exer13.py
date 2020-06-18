'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.'''

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

n = 1
resultado = 0
soma = 1


while(n <= (expoente + 1)):
    if n == 1:
        resultado = (base * base)
    else:
        soma = resultado * base
    resultado = soma
    n += 1

print(resultado)