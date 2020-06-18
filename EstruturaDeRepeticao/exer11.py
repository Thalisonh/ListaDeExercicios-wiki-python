'''Altere o programa anterior para mostrar no final a soma dos números.'''

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um novo número: "))

soma = 0

while(numero1 < numero2):
    numero1 += 1
    if numero1 == numero2:  
        break
    else:
        print(numero1)

    soma = soma + numero1

print(f'Soma: {soma}')