'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
anoAtual = date.today().year
contMenor = 0
contMaior = 0
for i in range(1, 7+1):
    anoNasc = int(input(f'Ano de nascimento da {i}ª pessoa: '))
    idade = anoAtual - anoNasc
    if idade < 18:
        contMenor += 1
    else:
        contMaior += 1
print(f'Ao todo tivemos {contMaior} pessoas maiores de idade.')
print(f'E também tivemos {contMenor} pessoas menores de idade.')
