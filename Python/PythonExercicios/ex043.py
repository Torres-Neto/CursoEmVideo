'''
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
from math import pow
peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / pow(altura, 2)
print('O IMC dessa pessoa é de \33[34m{:.1f}\33[m.'.format(imc))
if imc < 18.5:
    print('Você está \33[32mABAIXO DO PESO\33[m normal!')
elif imc <= 25:
    print('PARABÉNS, você está na faixa de \33[32mPESO NORMAL\33[m!')
elif imc <= 30:
    print('Você está com \33[32mSOBREPESO\33[m!')
elif imc <= 40:
    print('Você está em \33[32mOBESIDADE\33[m!')
else:
    print('Você está em \33[32mOBESIDADE MÓRBIDA\33[m, cuidado!')