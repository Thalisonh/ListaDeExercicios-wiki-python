'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.'''

#Resolução usando listas
n = 0

fibonacci = []

while(n < 20):
    if n == 0:
        fibonacci.append(0)
        fibonacci.append(1)
    else:
        fibonacci[n] = fibonacci[n - 1] + fibonacci[n - 2]
        fibonacci.append(fibonacci[n])
    n += 1

print(fibonacci[:-1])

'''
Resolução usando apenas variaveis 

n1 = 0
n2 = 1
count = 0

while count < 5:
    print(n1)
    resultado = n1 + n2
    n1 = n2
    n2 = resultado
    count += 1'''
    