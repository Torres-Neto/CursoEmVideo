# Ler um valor em metros e o exibir convertido em centímetros e milímetros.

m = float(input('Digite um valor em Metros(m): '))
cm = m * 100
mm = m * 1000
print('{}m são: {}cm e {}mm'.format(m, cm, mm))