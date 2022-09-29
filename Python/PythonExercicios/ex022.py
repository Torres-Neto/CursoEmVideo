'''
Criar um programa que leia o nome completo de uma pessoa e mostre:
>> O nome com todas as letras maiúsculas e minúsculas.
>> Quantas letras ao todo(sem considerar espaços).
>> Quantas letras tem o primeiro nome.
'''


nome = input('Digite seu nome completo: ').strip()
print('Seu nome em maíuscula é: ',nome.upper())
print('Seu nome em minúscula é: ',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))