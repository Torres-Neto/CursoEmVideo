'''
Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES.
Se o valor digitado for ÍMPAR, desconsidere-o.
'''

print('Digite agora, seis números:')
s = 0
for i in range(1, 6+1):
    n = int(input('Digite o número {}º número: '.format(i)))
    if n % 2 == 0:
        s += n
print(f'A soma dos números PARES digitados é: {s}.')