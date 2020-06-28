'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m'''

atleta = []
saltos_geral = []
media = []

n = 0
quantidade_atletas = int(input("Digite o número de atletas: "))
while n < quantidade_atletas:
    atleta.append(input("Digite o nome do atleta: "))
    saltos = []
    for i in range(5):
        saltos.append(float(input(f'Salto {i + 1}: ')))
    
    media = (sum(saltos) - max(saltos) - min(saltos)) / 3
    print()
    print(f'Atleta: {atleta[n]}')
    print(f'Primeiro Salto: {saltos[0]} m')
    print(f'Segundo Salto: {saltos[1]} m')
    print(f'Terceiro Salto: {saltos[2]} m')
    print(f'Quarto Salto: {saltos[3]} m')
    print(f'Quinto Salto: {saltos[4]} m ')
    print()
    print(f'Melhor Salto: {max(saltos)}')
    print(f'Pior Salto: {min(saltos)}')
    print(f'Média dos demais saltos: {media} m')
    print()
    print('Resultado final:')
    print(f'{atleta[n]}: {media} m')
    print()
    
    saltos_geral.append(saltos)
    
    n += 1
