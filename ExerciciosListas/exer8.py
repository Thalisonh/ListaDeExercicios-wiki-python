'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
'''

altura = []
idade = []

for i in range(5):
    altura.append(float(input("Altura: ")))
    idade.append(int(input("Idade: ")))

print()
for i in range(4, -1, -1):
    print(f'Altura: {altura[i]}')
    print(f'Idade: {idade[i]}')
    