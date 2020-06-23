'''O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.'''

n = 0
soma = 0
media = 0
maior = 0
menor = 0

quantidade_temperatura = int(input("Digite a quantidade de temperatuda: "))

temperatura = float(input("Digite a temperatura: "))
soma = soma + temperatura
maior = temperatura
menor = temperatura
while n < quantidade_temperatura - 1:
    temperatura = float(input("Digite a temperatura: "))
    soma = soma + temperatura
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
    n += 1

media = soma / (n + 1)

print(f'Menor: {menor}')
print(f'Maior: {maior}')
print(f'Média: {media}')

    
