# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. Com 5% de Desconto
preco = float(input('Qual o preço do produto? '))
desconto = preco - ((preco * 5) / 100)
print('O valr normal do produto é R${:.2f}.'.format(preco))
print('Com desconto de 5%. O produto custará R${:.2f}'.format(desconto))