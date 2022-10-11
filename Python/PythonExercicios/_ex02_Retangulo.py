'''
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.
'''

from math import hypot

base = float(input('Base do retângulo: '))
altura = float(input('Altura do retângulo: '))
print('Área = {:.4f}'.format(base*altura))
print('Perímetro = {:.4f}'.format((base*2) + (altura*2)))
print('Diagonal = {:.4f}'.format(hypot(base, altura)))