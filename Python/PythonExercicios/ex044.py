'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
- À vista DINHEIRO/CHEQUE: 10% de desconto
- À vista no CARTÃO: 5% de desconto
- Em até 2X NO CARTÃO: preço normal
- 3x OU MAIS no cartão: 20% de juros
'''


print('{:=^40}'.format(' LOJA TORRES '))
valor = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] À vista DINHEIRO/CHEQUE
[ 2 ] À vista no CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3x OU MAIS no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    pagamento = valor - (valor * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(
        valor, pagamento))
elif opcao == 2:
    pagamento = valor - (valor * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(
        valor, pagamento))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(valor/2))
    print(
        'Sua compra vai custar R${:.2f} no final, pois nessa condição o preço normal se mantém.'.format(valor))
elif opcao == 4:
    numeroParcelas = int(input('Quantas parcelas? '))
    if numeroParcelas >= 3:
        pagamento = valor + (valor * 20 / 100)
        valorParcela = pagamento / numeroParcelas
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(
            numeroParcelas, valorParcela))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(
            valor, pagamento))
    else:
        print('Quantidade de parcelas ABAIXO DO PERMITIDO nesta condição!')
else:
    print('OPÇÃO INVÁLIDA de pagamento. TENTE NOVAMENTE!')
