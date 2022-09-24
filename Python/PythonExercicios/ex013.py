# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Com 15% de aumento.

salario = float(input('Qual o salário atual do funcionário? '))
novoSalario = (salario * 15) / 100 + salario
print('O novo salário com aumento de 15% é: R${:.2f}'.format(novoSalario))