'''
Crie um programa que faça o computador jogar JOKENPÔ com você.
'''

from random import randint
from time import sleep
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
opcaoUsuario = int(input('Qual é a sua jogada? '))
if opcaoUsuario == 1 or opcaoUsuario == 2 or opcaoUsuario == 3:
    opcaoPC = randint(1, 3)
    print('JO...')
    sleep(1)
    print('KEN..')
    sleep(0.5)
    print('PO!!!')
    sleep(1)
    print('-='*12)
    if opcaoUsuario == 1:
        print('Você jogou PEDRA!')
    elif opcaoUsuario == 2:
        print('Você jogou PAPEL!')
    else:
        print('Você jogou TESOURA!')
    sleep(0.25)
    if opcaoPC == 1:
        print('Computador jogou PEDRA!')
    elif opcaoPC == 2:
        print('Computador jogou PAPEL!')
    else:
        print('Computador jogou TESOURA!')
    print('-='*12)
    sleep(1)
    if opcaoPC == 1 and opcaoUsuario == 2:
        print('Papel enrola a pedra: VOCÊ VENCEU!')
    elif opcaoPC == 1 and opcaoUsuario == 3:
        print('Pedra quebra a tesoura: COMPUTADOR VENCEU!')
    elif opcaoPC == 2 and opcaoUsuario == 1:
        print('Papel enrola a pedra: COMPUTADOR VENCEU!')
    elif opcaoPC == 2 and opcaoUsuario == 3:
        print('Tesoura corta o papel: VOCÊ VENCEU!')
    elif opcaoPC == 3 and opcaoUsuario == 1:
        print('Pedra quebra a tesoura: VOCÊ VENCEU!')
    elif opcaoPC == 3 and opcaoUsuario == 2:
        print('Tesoura corta o papel: COMPUTADOR VENCEU!')
    else:
        print('EMPATE!! JOGUEM NOVAMENTE')   
else:
    print('Escolha uma opção entre 1 e 3! tente novamente!')
print('')