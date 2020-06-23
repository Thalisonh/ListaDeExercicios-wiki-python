'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''

codigo = []
altura = []
peso = []
mais_alto = 0
mais_baixo = 0
mais_gordo = 0
mais_magro = 0


cod = int(input("Digite seu código: "))
altura2 = int(input("Digite sua altura: "))
peso2 = float(input("Digite seu peso: "))
codigo.append(cod)
altura.append(altura2)
peso.append(peso2)
while cod != 0:
    cod = int(input("Digite seu código: "))
    if cod == 0:
        break
    else: 
        altura2 = int(input("Digite sua altura: "))
        peso2 = float(input("Digite seu peso: "))
        codigo.append(cod)
        altura.append(altura2)
        peso.append(peso2)

for i in codigo:
    mais_alto = altura[0]
    mais_baixo = altura[0]
    mais_gordo = peso[0]
    mais_magro = peso[0]



