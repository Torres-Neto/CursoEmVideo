'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
A média de idade do grupo, 
Qual é o nome do homem mais velho e 
Quantas mulheres têm menos de 20 anos.
'''

somaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ''
totalMulher = 0
for i in range (1, 4 + 1):
    print(f'----- {i}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    print('')    
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1

mediaIdades = somaIdade / i
print('A média de idade do grupo é de {:.2f} anos.'.format(mediaIdades))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeMaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher))