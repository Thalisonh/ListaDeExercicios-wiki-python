'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

metro = float(input('Qual a area a ser pintada? (em metros quadrados) '))
margem = metro * 1.1
print('Metragem com margem de 10%: ',int(margem),'m²'  )

quantidade_latas = margem // 108
quantidade_galoes = margem // 21.6

if margem % 108 > 0: #primeira situacao
    quantidade_latas = quantidade_latas + 1

preco_lata = quantidade_latas*80    
print('Se comprar somente latas, o preco sera %i comprando %i latas' % (preco_lata, quantidade_latas))

if margem % 21.6 > 0: #segunda situacao  
    quantidade_galoes = quantidade_galoes + 1
    
preco_galoes = quantidade_galoes * 25    
print('Se comprar somente galoes, o preco sera',preco_galoes,'comprando',quantidade_galoes,'galoes')

if margem % 108 > 0:
    quantidade_latas2 = margem // 108
    sobra = (margem / 108 - margem // 108) * 108
    quantidade_galoes = sobra // 21.6
    
    if sobra % 21.6 > 0:    
        quantidade_galoes = quantidade_galoes + 1
    
preco_lata2 = quantidade_latas2 * 80    
preco_galoes2 = quantidade_galoes * 25
precototal = preco_lata2 + preco_galoes2    
print('A quantidade de latas e',quantidade_latas2,'e a quantidade de galoes e',quantidade_galoes,', o preco total e',precototal)