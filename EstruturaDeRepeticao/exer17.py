'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

num = 1
fat = 1
n1 = int(input("Digite um número: "))
if n1 == 0 or n1 == 1:
    print(f'Fatorial de 0 ou 1 = {fat}')
else:
    while n1 > 0:
        fat = n1 * num
        num = fat
        n1 -= 1

print(fat)
