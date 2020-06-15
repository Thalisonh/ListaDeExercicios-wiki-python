'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 != 0:
        if dia > 0 and dia <= 29:
            print("Data válida!")
        else:
            print("Data inválida")
else:
    if dia > 0 and dia <= 28:
        print("Data válida!")
    else:
        print("Data inválida")
