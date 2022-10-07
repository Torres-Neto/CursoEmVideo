'''
Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500
'''
s = 0
for i in range (1, 500):
    if i % 3 == 0:
        s += i
print('A soma dos múltiplos de 3 entre 1 e 500 é: \33[32m{}\33[m'.format(s))