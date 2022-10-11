'''
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
print('='*30)
print('10 TERMOS DE UMA P.A.')
print('='*30)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range (termo, 10*razao+termo, razao):
    print(f'{i}', end='  >> ')
print('ACABOU!')