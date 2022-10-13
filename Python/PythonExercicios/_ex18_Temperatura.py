'''
Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com
duas casas decimais.
'''

escala = input('Você vai digitar a temperatura em qual escala (C/F)? ').strip()
if escala in 'Ff':
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
    celsius = (fahrenheit - 32) * 5/9
    print(f'Temperatura equivalente em Celsius: {celsius:.2f}°F')
else:
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f'Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}°C')
print('')