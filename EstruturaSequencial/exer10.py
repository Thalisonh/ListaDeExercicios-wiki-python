'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.'''

temp_celsius = float(input("Digite a a temperatura em Celsius: "))

temp_fahrenheit = (temp_celsius * (9 / 5) + 32)

print(f'{temp_celsius}ºC em Fahrenheit é: {temp_fahrenheit}ºF')