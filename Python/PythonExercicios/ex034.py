'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 calcule um aumento de 10%.
Para salárior inferiores ou iguais, o aumento é de 15%
'''

salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    aumento = 10
else:
    aumento = 15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, (salario * aumento)/100 + salario))
