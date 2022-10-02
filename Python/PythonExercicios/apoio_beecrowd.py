cod1 = int(input('Código: '))
quant1 = int(input('Quantidade: '))
valor1 = float(input('Preço: '))

cod2 = int(input('Código: '))
quant2 = int(input('Quantidade: '))
valor2 = float(input('Preço: '))

pagto = (quant1 * valor1) + (quant2 * valor2)

print('VALOR A PAGAR: R$ {}'.format(pagto))