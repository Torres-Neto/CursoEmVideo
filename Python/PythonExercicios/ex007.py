# Desenvolver um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = float(input('Qual a Primeira nota do aluno? '))
n2 = float(input('Qual a Segunda nota do aluno? '))

media = (n1 + n2)/2

print('O aluno ficou com média: {:.2f}.'.format(media))