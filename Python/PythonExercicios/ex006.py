# Criar um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math



n = int(input('Digite um número: '))
print('Você digitou o número', n)
print('O Dobro de {} é {}!'.format(n, n*2))
print('O Triplo de {} é {}!'.format(n, n*3))
print('A Raiz Quadrada de {} é {:.2f}!'.format(n, math.sqrt(n)))