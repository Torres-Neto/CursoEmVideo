# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for i in range (1, 5+1):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        elif menor > peso:
            menor = peso
print('O maior peso lido foi de {:.2f}Kg'.format(maior))
print('O menor peso lido foi de {:.2f}Kg'.format(menor))
