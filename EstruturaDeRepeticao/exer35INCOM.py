'''Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.'''

numero = int(input("Digite um numero: "))
n = numero
j = 1
flag = 0

while n > 0:
    while j < numero:
        if n % j == 0:
            flag += 1
            if flag < 2:
                print(n)
                n -= 1
            else:
                flag = 0
        j += 1
    n -= 1
