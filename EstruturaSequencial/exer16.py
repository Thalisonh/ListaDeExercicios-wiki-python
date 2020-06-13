#importa biblioteca matemática
import math 

'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

tamanho = float(input("Digite o tamanho da area a ser pintada: "))

quantidade_tintas = tamanho / 3
#função ceil arredonda o valor pra cima
lata_tinta = math.ceil(quantidade_tintas / 18)
preco = lata_tinta * 80

print('A quantidade de tinta necessária para pintar {:.1f}m² é de {:.0f} latas e o valor total é de R${:.2f}'.format(tamanho, lata_tinta, preco))

