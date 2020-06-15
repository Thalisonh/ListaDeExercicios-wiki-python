'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

semana = int(input("Digite um número: "))

if semana == 1:
    print(f'{semana}-Domingo')
elif semana == 2:
    print(f'{semana}-Segunda')
elif semana == 3:
    print(f'{semana}-Terça')
elif semana == 4:
    print(f'{semana}-Quarta')
elif semana == 5:
    print(f'{semana}-Quinta')
elif semana == 6:
    print(f'{semana}-Sexta')
elif semana == 7:
    print(f'{semana}-Sábado')
else:
    print('Número inválido!')