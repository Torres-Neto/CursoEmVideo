'''
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
uma mensagem explicativa.
'''

nome = input('Nome: ')
valorHora = float(input('Valor por hora: '))
horasTrabalhadas = float(input('Horas trabalhadas: '))
pagamento = valorHora * horasTrabalhadas
print(f'O pagamento para {nome} deve ser {pagamento:.2f}')