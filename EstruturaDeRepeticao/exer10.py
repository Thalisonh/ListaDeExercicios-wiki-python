'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um novo número: "))

while(numero1 < numero2):
    numero1 += 1
    if numero1 == numero2:  
        break
    else:
        print(numero1)

