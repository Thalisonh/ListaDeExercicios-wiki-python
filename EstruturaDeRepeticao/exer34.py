'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''

numero = int(input("Digite um número: "))
n = 1
flag = 0

while n < numero:
    if numero % n == 0:
        flag += 1
    n += 1
if flag > 2:
    print("Número não é primo!")
else:
    print("Número é primo!")
    
