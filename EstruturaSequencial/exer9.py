'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).'''

temp_fahrenheit = float(input("Digite a temperatura em Farenheit: "))

temp_celsius = (temp_fahrenheit - 32) * (5 / 9)

print(f'{temp_fahrenheit}ºF em Celsius é: {temp_celsius}ºC')