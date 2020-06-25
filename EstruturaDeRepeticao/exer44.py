'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''

votos = 1
thalison = 0
henrique = 0
morais = 0
silva = 0
nulo = 0
branco = 0
total = 0


print("1 - Thalison")
print("2 - Henrique")
print("3 - Morais")
print("4 - Silva")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print()

while votos != 0:
    votos = int(input("Voto: "))
    if votos == 1:
        thalison += 1
        total += 1

    elif votos == 2:
        henrique += 1
        total += 1

    elif votos == 3:
        morais += 1
        total += 1

    elif votos == 4:
        silva += 1
        total += 1

    elif votos == 5:
        nulo += 1
        total += 1

    elif votos == 6:
        branco += 1
        total += 1

porcentagem_nulos = (nulo / total) * 100
porcentagem_branco = (branco / total) * 100

print(f'Thalison: {thalison}')
print(f'Henrique: {henrique}')
print(f'Morais: {morais}')
print(f'Silva: {silva}')
print(f'Nulos: {nulo}')
print(f'Brancos: {branco}')
print('Porcentagem nulos: {:.2f}%'.format(porcentagem_nulos))
print('Porcentagem brancos: {:.2f}%'.format(porcentagem_branco))