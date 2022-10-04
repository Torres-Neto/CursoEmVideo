'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprados e em QUANTOS ANOS ele vai pagar.
Calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valorCasa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
tempoFinanciamento = int(input('Quantos anos de financiamento? '))

valorPrestacao = valorCasa / (tempoFinanciamento * 12)
porcentagem = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valorCasa, tempoFinanciamento, valorPrestacao))
if valorPrestacao > porcentagem:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
