'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = input("Digite seu nome: ")
while(len(nome) < 3):
    nome = input("Nome inválido, digite um novo nome: ")

idade = int(input("Digite sua idade: "))
while(idade < 0 or idade > 150):
    idade = int(input("Idade inválida, digite uma nova idade: "))

salario = float(input("Digite seu salário: "))
while(salario < 0):
    salario = float(input("Salário invávlido, digite um novo salário: "))

sexo = input("Digite seu sexo, (f) para feminino, (m) para masculino: ")
while(sexo != 'f' and sexo != 'm'):
    sexo = input("Sexo inválido, digte um novo sexo: ")

estado_civil = ("Digite a inicial do estado civil (s, c, v, d): ")
while(estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd'):
    estado_civil = input("Digite um novo estado civil: ")

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print('Salario: R${:.2f}'.format(salario))
print(f'Sexo: {sexo}')
print(f'Estado civil: {estado_civil}')
