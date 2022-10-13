'''
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
valor restante.
'''

preco = float(input('Preço unitário do produto: '))
quantidade = int(input('Quantidade comprada: '))
valorRecebido = float(input('Dinheiro recebido: '))
troco = valorRecebido - (preco * quantidade)
if troco == 0:
    print('O dinheiro está correto. Muito Obrigado!')
elif troco > 0:
    print(f'Seu troco é = {troco:.2f} Reais.')
else:
    print(f'Dinheiro insuficiente. Faltam {abs(troco):.2f} Reais.')
