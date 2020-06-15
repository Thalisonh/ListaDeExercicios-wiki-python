'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

valor_hora = float(input("Digite o valor hora: "))
hora_trabalhada = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = valor_hora * hora_trabalhada
inss = 10
fgts = 11

if salario_bruto <= 900:
    ir = 0
    calculo_ir = salario_bruto * ir
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = 5
    calculo_ir = salario_bruto * (ir / 100)
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = 10
    calculo_ir = salario_bruto * (ir / 100)
else:
    ir = 20
    calculo_ir = salario_bruto * (ir / 100)

calculo_inss = salario_bruto * (inss / 100)
calculo_fgts = salario_bruto * (fgts / 100)

total_descontos = calculo_inss + calculo_ir

salario_liquido = salario_bruto - calculo_inss - calculo_ir

print('Salário Bruto: ({:.2f} * {:.2f} = R${:.2f})'.format(valor_hora, hora_trabalhada, salario_bruto))
print('(-) IR ({:.0f}%) = R$ {:.2f}'.format(ir, calculo_ir))
print('(-) INSS ({:.0f}%) = R$ {:.2f}'.format(inss, calculo_inss))
print('(-) FGTS ({:.0f}%) = R$ {:.2f}'.format(fgts, calculo_fgts))
print('Total de descontos = R$ {:.2f}'.format(total_descontos))
print('Salário Liquido = R$ {:.2f}'.format(salario_liquido))
