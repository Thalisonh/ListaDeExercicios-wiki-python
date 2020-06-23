'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

soma = 0
media = 0

qtd_cds = int(input("Digite a quantidade de CDs: "))

for i in range(qtd_cds):
    valor_cds = float(input("Digite o valor do CD: "))
    soma = soma + valor_cds

media = soma / qtd_cds

print('A soma dos Cds é: R${:.2f}'.format(soma))
print('A média de preço é de R${:.2f}'.format(media))
