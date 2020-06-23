'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''

num = 1
fat = 1
n1 = int(input("Digite um número: "))
cont = n1
if n1 == 0 or n1 == 1:
    print(f'Fatorial de 0 ou 1 = {fat}')
else:
    while n1 > 0:
        fat = n1 * num
        num = fat
        n1 -= 1

print(f'{cont}! = ', end='')
while cont > 0:
    print(f'{cont} ', end='')
    if cont != 1:
        print('. ', end='')
    else:
        print("= ", end='')
        print(fat)
    cont -= 1