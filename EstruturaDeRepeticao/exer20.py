'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.'''

num = 1
fat = 1

print("Digite 0 para sair.")
entrada = int(input("Digite qualquer número para começar: "))
if entrada != 0:
    n1 = int(input("Digite um número: "))
    if n1 < 0 or n1 > 16:
        n1 = int(input("Digite um número: "))
        
    if n1 == 0 or n1 == 1:
        print(f'Fatorial de 0 ou 1 = {fat}')
    else:
        while n1 > 0:
            fat = n1 * num
            num = fat
            n1 -= 1
else:
    entrada = int(input("Digite um número: "))

print(fat)