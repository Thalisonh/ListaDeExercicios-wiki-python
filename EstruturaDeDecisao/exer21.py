'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

saque = float(input("Digite o valor a ser retirado: "))

cem = saque // 100
cinquenta = (saque - (cem * 100)) // 50
dez =  (saque - ((cinquenta * 50) + (cem * 100))) // 10
cinco = (saque - ((cinquenta * 50) + (cem * 100) + (dez * 10))) // 5
um = saque - ((cem * 100) + (cinquenta * 50) + (dez * 10) + (cinco * 5))

print('R$ {:.2f}'.format(saque))
if cem != 0:
    print(f'{cem} notas de cem')
if cinquenta != 0:
    print(f'{cinquenta} notas de cinquenta')
if dez != 0:
    print(f'{dez} notas de dez')
if cinco != 0:
    print(f'{cinco} notas de cinco')
if um != 0:
    print(f'{um} notas de um')