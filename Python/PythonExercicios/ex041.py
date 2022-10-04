'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''

from datetime import date
anoNascimento = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print('O atleta tem {} anos.'.format(idade))
if idade > 20:
    print('Classificação: \33[32mMASTER.\33[m')
elif idade > 19:
    print('Classificação: \33[32mSÊNIOR.\33[m')
elif idade > 14:
    print('Classificação: \33[32mJÚNIOR.\33[m')
elif idade > 9:
    print('Classificação: \33[32mINFANTIL.\33[m')
elif idade <= 9:
    print('Classificação: \33[32mMIRIM.\33[m')