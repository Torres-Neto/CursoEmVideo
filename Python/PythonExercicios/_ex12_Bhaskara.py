'''
Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com duas casas decimais,
conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.
'''

import math


print('--- FÓRMULA DE BHÁSKARA ---')
a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))
delta = pow(b, 2)-4*a*c
if delta < 0:
    print('Esta equação não possui raízes reais.')
else:
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a
    if a == 0:
        print('O valor de \33[32ma\33[m, deve ser diferente de \33[32m0\33[m')
    elif delta == 0:
        print('Esta equação possui apenas uma raiz real')
        print('X1 = {:.4f}'.format(x1))
    elif delta > 0:
        print('Esta equação possui duas raízes reais.')
        print('X1 = {:.2f}'.format(x1))
        print('X2 = {:.2f}'.format(x2))
print('-----------------------------')