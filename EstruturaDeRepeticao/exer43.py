'''O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.'''

print("Especificação   Código  Preço")
print("Cachorro Quente 100     R$ 1,20")
print("Bauru Simples   101     R$ 1,30")
print("Bauru com ovo   102     R$ 1,50")
print("Hambúrguer      103     R$ 1,20")
print("Cheeseburguer   104     R$ 1,30")
print("Refrigerante    105     R$ 1,00")

total = 0
codigo = 1
while codigo != 0:
    print("Digite 0 para finalizar.")
    codigo = int(input("Código: "))
    if codigo == 100:
        quantidade = int(input("Quantidade: "))
        total = total + (quantidade * 1.20)

    elif codigo == 101:
        quantidade = int(input("Quantidade: "))
        total = total + (quantidade * 1.30)

    elif codigo == 102:
        quantidade = int(input("Quantidade: "))
        total = total + (quantidade * 1.50)

    elif codigo == 103:
        quantidade = int(input("Quantidade: "))
        total = total + (quantidade * 1.20)

    elif codigo == 104:
        quantidade = int(input("Quantidade: "))
        total = total + (quantidade * 1.30)

    elif codigo == 105:
        quantidade = int(input("Quantidade: "))
        total = total + (quantidade * 1.00)

print('Valor total: R${:.2f}'.format(total))
