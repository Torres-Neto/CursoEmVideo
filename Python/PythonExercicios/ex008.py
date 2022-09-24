# Ler um valor em metros e o exibir convertido em centímetros e milímetros.

m = int(input('Uma distância em Metros(m): '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {}m corresponde a:'.format(float(m)))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
print('')