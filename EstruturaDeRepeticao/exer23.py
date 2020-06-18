'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''

numero = int(input("Digite um numero: "))

n = 1
flag = 0
cont = 0
while n < numero:
    if numero % n == 0:
        cont += 1
        print(n)
        flag += 1
        n += 1
    else:
        cont += 1
        n += 1

if flag == 1:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')

print(f'Número de divisões: {cont}')