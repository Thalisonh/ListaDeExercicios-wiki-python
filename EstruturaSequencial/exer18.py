'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

arquivo = float(input("Digite o tamanho do arquivo em MB: "))
link = float(input("Digite a velocidade de internet: "))

tempo = arquivo / link
tempo_minuto = tempo // 60
tempo_segundo = tempo - tempo_minuto

print('O tempo aproximado de download e {:.0f} minutos e {:.0f} segundos'.format(tempo_minuto, tempo_segundo))