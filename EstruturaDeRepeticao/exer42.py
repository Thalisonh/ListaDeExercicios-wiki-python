'''Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.'''

n = 0

cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while n >= 0:
    n = int(input("Digite um número: "))
    if n > 0 and n <= 25:
        cont_0_25 += 1
    elif n > 25 and n <= 50:
        cont_26_50 += 1
    elif n > 50 and n <= 75:
        cont_51_75 += 1
    elif n > 75 and n <= 100:
        cont_76_100 += 1

print(f'Intervalo [0-25]: {cont_0_25}')
print(f'Intervalo [26-50]: {cont_26_50}')
print(f'Intervalo [51-75]: {cont_51_75}')
print(f'Intervalo [76-100]: {cont_76_100}')