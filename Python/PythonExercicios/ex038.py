'''
Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
- o PRIMEIRO VALOR é MAIOR:
- o SEGUNDO VALOR é MAIOR:
- NÃO EXISTE valor maior, os dois são IGUAIS.
'''

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num1 < num2:
    print('O SEGUNDO valor é maior.')
else:
    print('NÃO EXISTE valor maior, os dois são iguais.')