'''
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.
'''

preco = float(input('Preço unitário do produto: '))
quantidade = int(input('Quantidade comprada: '))
valorRecebido = float(input('Dinheiro recebido: '))
total = preco * quantidade
troco = valorRecebido - total
print(f'TROCO = {troco:.2f}')