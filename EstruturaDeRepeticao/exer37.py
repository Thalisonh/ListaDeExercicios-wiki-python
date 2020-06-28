'''Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes'''

codigo = []
altura = []
peso = []
mais_alto = 0
mais_baixo = 0
mais_gordo = 0
mais_magro = 0

numero_usuarios = int(input("Digite o número de usúarios: "))

for i in range(numero_usuarios):
    codigo.append(int(input("Digite seu código: ")))
    altura.append(int(input("Digite sua altura: ")))
    peso.append(float(input("Digite seu peso: ")))

mais_alto = max(altura)
mais_baixo = min(altura)
mais_gordo = max(peso)
mais_magro = min(peso)

for i in range(numero_usuarios):
    if mais_alto == altura[i]:
        print(f'Codigo: {codigo[i]} mais alto {mais_alto} cm.')
    elif mais_baixo == altura[i]:
        print(f'Código: {codigo[i]} mais baixo {mais_baixo} cm.')
    if mais_gordo == peso[i]:
        print(f'Código: {codigo[i]} mais gordo {mais_gordo} kg.')
    if mais_magro == peso[i]:
        print(f'Cógido: {codigo[i]} mais magro {mais_magro} kg.')