'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes
'''

print('-='*12)
print('Analisador de Triângulos')
print('-='*12)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    if seg1 == seg2 == seg3:
        print('Os segmentos acima PODEM FORMAR um triângulo do tipo EQUILÁTERO: todos os lados iguais.')
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        print('Os segmentos acima PODEM FORMAR um triângulo do tipo ISÓSCELES: dois lados iguais.')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo do tipo ESCALENO: todos os lados diferentes.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
