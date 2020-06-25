'''Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67'''

valor_divida = float(input("Digite o valor da divída: "))

print()
print("Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida")
print("1 - 0%")
print("3 - 10%")
print("6 - 15%")
print("9 - 20%")
print("12 - 25%")

print()
print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
parcela = 0
n = 1
while(n <= 12):
    if n == 1:
        quantidade_parcela = 1
        juros = valor_divida * 0
        parcela = (valor_divida * juros) / 1
        total = valor_divida + juros
        print('R${:.2f}                {:.0f}                   {:.0f}                  R${:.2f}'.format(total, juros, quantidade_parcela, parcela))

    if n == 3:
        quantidade_parcela = 3
        juros = valor_divida * 0.10
        total = valor_divida + juros
        parcela = total / quantidade_parcela
        print('R${:.2f}              {:.0f}                   {:.0f}                  R${:.2f}'.format(total, juros, quantidade_parcela, parcela))

    if n == 6:
        quantidade_parcela = 6
        juros = valor_divida * 0.15
        total = valor_divida + juros
        parcela = total / quantidade_parcela
        print('R${:.2f}              {:.0f}                   {:.0f}                  R${:.2f}'.format(total, juros, quantidade_parcela, parcela))

    if n == 9:
        quantidade_parcela = 6
        juros = valor_divida * 0.20
        total = valor_divida + juros
        parcela = total / quantidade_parcela
        print('R${:.2f}              {:.0f}                   {:.0f}                  R${:.2f}'.format(total, juros, quantidade_parcela, parcela))

    if n == 12:
        quantidade_parcela = 12
        juros = valor_divida * 0.25
        total = valor_divida + juros
        parcela = total / quantidade_parcela
        print('R${:.2f}              {:.0f}                   {:.0f}                 R${:.2f}'.format(total, juros, quantidade_parcela, parcela))
    n += 1