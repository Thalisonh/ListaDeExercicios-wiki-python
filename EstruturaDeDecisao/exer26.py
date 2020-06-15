'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: 
até 20 litros, desconto de 3% por litro 
acima de 20 litros, desconto de 5% por litro

Gasolina: 
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

litros = float(input("Digite a quantidade de litros: "))
combustivel = input("Digite o combustivel (A - álcool) (G - gasolina): ")

gasolina = 2.50
alcool = 1.90

if combustivel == 'A':
    if litros <= 20:
        desconto = ((litros * 3) / 100) * alcool
        total = (alcool * litros) - desconto
    else:
        desconto = ((litros * 5) / 100) * alcool
        total = (alcool * litros) - desconto

if combustivel == 'B':
    if litros <= 20:
        desconto = ((litros * 4) / 100) * gasolina
        total = (gasolina * litros) - desconto
    else:
        desconto = ((litros * 6) / 100) * gasolina
        total = (gasolina * litros) - desconto

print('O preço pago por {:.0f}l de {} é de R${:.2f}'.format(litros, combustivel, total))