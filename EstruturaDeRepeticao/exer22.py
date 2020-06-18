'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.'''

numero = int(input("Digite um numero: "))

n = 1
flag = 0
nao_primo = []
while n < numero:
    if numero % n == 0:
        nao_primo.append(n)
        n += 1
    else:
        flag += 1
        n += 1

if flag == 1:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')

print(f'É divisível por {nao_primo}')