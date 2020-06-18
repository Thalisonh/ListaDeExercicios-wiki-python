'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

eleitores = int(input("Digite o número de eleitores: "))
cont = 0

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

while cont < eleitores:
    voto = int(input("Digite seu voto: "))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2: 
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    else:
        print("Voto inválido.")
    cont += 1

print(f'Candidato_1: {candidato_1}')
print(f'Candidato_2: {candidato_2}')
print(f'Candidato_3: {candidato_3}')