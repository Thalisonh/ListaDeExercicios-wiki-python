'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

numero_pessoas = int(input("Digite o número de pessoas: "))

cont = 0
soma = 0

while cont < numero_pessoas:
    idade = int(input("Digite a sua idade: "))
    soma = soma + idade
    cont += 1

media = soma / cont
if media > 0 and media <= 25:
    print("A média varia de 0 - 25 anos, TURMA JOVEM")
elif media > 25 and media <= 60:
    print("A média varia de 26 - 60 anos, TURMA ADULTA")
elif media > 60:
    print("A média varia de 60 ou mais, TURMA IDOSA")
    
print(f'A média de idade da turma é: {media}')