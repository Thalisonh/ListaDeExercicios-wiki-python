'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.'''


limite = int(input("Digite um número: "))
numero = 2
c = 1
p = 0
print("Primos:")
while numero < limite:
    i = numero -1
    while i > 1:
        if numero % i == 0: break
        i -= 1
        c += 1
    else:
        print(numero),
        p += 1
    numero += 1
