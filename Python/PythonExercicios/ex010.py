# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considerando U$1,00 = R$3,27

real = float(input('Quantos Reais você tem? '))
dolar = real / 3.27
print('Com {} reais é possível comprar {:.2f} dólares.'.format(real, dolar))