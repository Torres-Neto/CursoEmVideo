'''
Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
números lidos. Em caso de empate, mostrar apenas uma vez.
'''

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
if v1 < v2 < v3:
    print(f'MENOR = {v1}')
elif v2 < v1 < v3:
    print(f'MENOR = {v2}')
else:
    print(f'MENOR = {v3}')