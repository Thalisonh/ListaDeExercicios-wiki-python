'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

morango = float(input("Digite a quantidade em Kg de morangos: "))
if morango <=5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20
maca = float(input("Digite a quantidade em Kg de maçãs: "))
if maca <= 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50

total = preco_morango + preco_maca

if (morango + maca) > 8 or total > 25:
    desconto = total - (total * 0.10)
else:
    desconto = total

print('O valor a ser pago pelo cliente é de: R${:.2f}'.format(desconto))
