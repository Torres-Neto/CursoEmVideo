"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
"""
from time import sleep
import emoji
print('VAMOS CELEBRAR O NOVO ANO!!')
for i in range(10, -1, -1):
    print(f'{i}...')
    sleep(1.2)
print('FELIZ ANO NOVOO!!!!')
print(emoji.emojize('🙌🎇🎆🎇👨‍💻🎆🎇🎆🙌'))
print('')