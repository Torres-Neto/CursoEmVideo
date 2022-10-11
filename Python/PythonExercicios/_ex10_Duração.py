'''
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.
'''

segundos = int(input('Digite a duração em segundos: '))
h = segundos // 3600
resto = segundos % 3600
m = resto // 60
s = resto % 60
print(f'{h}h {m}m {s}s')