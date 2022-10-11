'''
Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500
'''
s = 0
cont = 0
for i in range (1, 500+1):
    if i % 2 != 0 and i % 3 == 0:
        cont += 1
        s += i
print('A soma de todos os \33[32m{}\33[m valores solicitados é: \33[32m{}\33[m'.format(cont, s))
