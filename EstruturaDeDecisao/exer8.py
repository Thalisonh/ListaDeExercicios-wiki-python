'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

preco1 = float(input("Digite o preço: "))
preco2 = float(input("Digite o preço: "))
preco3 = float(input("Digite o preço: "))

if preco1 > preco2:
    menor = preco2
else:
    menor = preco1

if preco3 < menor:
    menor = preco3

print(menor)