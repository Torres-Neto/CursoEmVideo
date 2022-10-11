'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
print('Descubra se um número é primo!')
numero = int(input('Digite um número: '))
count = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        count += 1
        print(f'\33[32m{i}\33[m', end=' ')
    else:
        print(f'\33[34m{i}\33[m', end=' ')
print('\nO número {} foi divisível {} vezes:'.format(numero, count))
if count == 2:
    print('E por isso ele É PRIMO!')
elif numero == 0:
    print('O Zero NÃO É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')