'''
Faça um Programa que leia um vetor de N caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

letras = input("Digite uma palavra: ").upper()
consoantes = 0

for i in letras:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        pass
    else:
        consoantes += 1

print(f'Foram lidas: {consoantes} consoantes.')