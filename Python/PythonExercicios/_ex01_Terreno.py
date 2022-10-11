'''
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
duas casas decimais, conforme exemplo.
'''

larg = float(input('Digite a largura do terreno: '))
comp = float(input('Digite o comprimento do terreno: '))
metroQuadrado = float(input('Digite o valor do metro quadrado: '))
print('Área do terreno = {:.2f}'.format(larg*comp))
print('Preço do terreno = {:.2f}'.format((larg*comp)*metroQuadrado))