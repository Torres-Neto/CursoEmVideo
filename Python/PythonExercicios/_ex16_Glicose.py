'''
Fazer um programa para ler a quantidade de glicose
no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose de acordo com a tabela de
referência ao lado.
'''

medida = float(input('Digite a medida da glicose: '))
if medida <= 100:
    print('Classificação: \33[32mNormal\33[m')
elif medida <= 140:
    print('Classificação: \33[33mElevado\33[m')
else:
    print('Classificação: \33[31mDIABETES\33[m')