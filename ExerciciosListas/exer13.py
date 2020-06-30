'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

temperaturas = []
soma = 0
media = 0

n = 0
while n < 12:
    temp = float(input(f'Digite a temperatura média de {meses[n]}: '))
    temperaturas.append(temp)
    soma = soma + temp
    n += 1

media = soma / 12

n = 0
while n < 12:
    if temperaturas[n] > media:
        print(f'Temperatura: {n}-{meses[n]} - {temperaturas[n]}')
    n += 1