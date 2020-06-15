'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

quantidade_carne = float(input("Digite a quantidade de carne: "))
if quantidade_carne <= 5:
    file = 4.90
    alcatra = 5.90
    picanha = 6.90
else:
    file = 5.80
    alcatra = 6.80
    picanha = 7.80

tipo_carne = input("Digite o tipo da carne: ")
if tipo_carne == 'file':
    total = file * quantidade_carne
elif tipo_carne == 'alcatra':
    total = alcatra * quantidade_carne
elif tipo_carne == 'picanha':
    total = picanha * alcatra

cartao = input("A compra foi feita no cartão: ")
if cartao == 'sim':
    desconto = 0.05 * total
else:
    desconto = 0 * total

total_desconto = total - desconto

print('Carne: {} {:.2f}Kg'.format(tipo_carne, quantidade_carne)) 
print('Preço total: R${:.2f}'.format(total)) 
print('Cartão: {}'.format(cartao))
print('Valor do desconto: R${:.2f}'.format(desconto))
print('Valor a pagar: {:.2f}'.format(total_desconto))