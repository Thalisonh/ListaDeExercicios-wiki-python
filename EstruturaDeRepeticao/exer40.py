'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
A - Código da cidade;
B - Número de veículos de passeio (em 1999);
C - Número de acidentes de trânsito com vítimas (em 1999). 

Deseja-se saber:
D - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
E - Qual a média de veículos nas cinco cidades juntas;
F - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

cidade = []
veiculos = []
acidentes = []

for i in range(5):
    cidade.append(int(input("Codigo: ")))
    veiculos.append(int(input("Veículos: ")))
    acidentes.append(int(input("Acidentes: ")))

menor = min(acidentes)
maior = max(acidentes)
media = sum(veiculos) / 5
media_2000 = 0

for i in range(5):
    if maior == acidentes[i]:
        print(f'A cidade de {cidade[i]} tem o maior indíce de acidentes.')
    if menor == acidentes[i]:
        print(f'A cidade de {cidade[i]} tem o menor indíce de acidentes.')
    if veiculos[i] < 2000:
        media_2000 = media_2000 + veiculos[i]

print(f'A média de veículos nas cinco cidades é: {media}')
print(f'A média de acidentes de trânsito nas cidades com menos de 2.000 veículos: {media_2000}')
    