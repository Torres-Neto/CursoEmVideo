'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR:
'''
numero = int(input('Me diga um número qualquer: '))
if numero % 2 == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é ÍMPAR.'.format(numero))
