'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''
n = True
while(n):
    numero = int(input("Digite uma nota: "))
    if numero < 0 or numero > 10:
        n = True
    else:
        n = False
    