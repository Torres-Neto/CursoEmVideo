'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200km
e R$0,45 para viagens mais longas.
'''

distancia = float(input('Digite a distância da sua viagem? '))
print('Você está  prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(valor))
