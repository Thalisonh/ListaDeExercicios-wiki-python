'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input("Digite um salário: "))

if salario <= 280:
    percentual = 0.20
    aumento = salario * percentual
elif salario > 280 and salario <= 700:
    percentual = 0.15
    aumento = salario * percentual
elif salario > 700 and salario <= 1500:
    percentual = 0.10
    aumento = salario * percentual
else:
    percentual = 0.05
    aumento = salario * percentual

novo_salario = salario + aumento

print(f'O salário era de R${salario}, o percentual aplicado foi de {percentual * 100}%, o valor do aumento foi de R${aumento} e o novo salário é de R${novo_salario}')