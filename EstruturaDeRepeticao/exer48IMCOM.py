'''Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321'''

numero = int(input("Digite um número: "))

numeroInvertido = int(str(numero)[::-1])
print(f'Numero invertido: {numeroInvertido}')


