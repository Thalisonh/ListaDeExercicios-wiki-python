'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
'''

numeros = []
soma = 0
contador = 0
media = 0

n = 0
while n != -1:
    numero = int(input("Digite um número: "))
    if numero != -1:
        numeros.append(numero)
        soma = soma + numero
        contador += 1
    n = numero

cont = contador

media = sum(numeros) / contador
acima_media = 0
abaixo_sete = 0

print()
print("Números: ", end='')
for i in numeros:
    if i > media:
        acima_media += 1
    if i < 7:
        abaixo_sete += 1
    print(f'{i} ', end='')

print()
print("Números invertidos: ", end='')
n = 0
while cont > n:
    print(f'{cont} ', end='')
    cont -= 1

print()
print(f'Soma: {sum(numeros)}')
print(f'Média: {media}')
print(f'Valores acima da média: {acima_media}')
print(f'Valores abaixo de 7: {abaixo_sete}')
print('Programa finalizado.')
print()