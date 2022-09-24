'''
Faça um programa que leia uma largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la
Sabendo que cada litro de tinta, pinta uma área de 2m².
'''

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura? '))
areaParede = largura * altura
litroTinta = areaParede / 2

print('Para pintar uma parede com largura {}m e altura {}m, serão necessários {:.2f} litros de tinta.'.format(largura, altura, litroTinta))