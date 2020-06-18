'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.'''

a = int(input("Digite a população A: "))
crescimento_A = float(input("Digite a taxa de crescimento A: "))
b = int(input("Digite a população B: "))
crescimento_B = float(input("Digite a taxa de crescimento B: "))

ano = 0
while(a < b):
    a = a + (a * (crescimento_A / 100))
    b = b + (b * (crescimento_B / 100))
    ano += 1

print('População A: {:.0f} habitantes'.format(a))
print('População B: {:.0f} habitantes'.format(b))
print(f'Ano: {ano}')