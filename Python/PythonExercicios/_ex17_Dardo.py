'''
No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
foi a maior.
'''
print('Digite as três distâncias:')
dist1 = float(input('1ª: '))
dist2 = float(input('2ª: '))
dist3 = float(input('3ª: '))
if dist1 > dist2 and dist1 > dist3:
    print(f'MAIOR DISTÂNCIA = {dist1:.2f}')
elif dist2 > dist1 and dist2 > dist3:
    print(f'MAIOR DISTÂNCIA = {dist2:.2f}')
else:
    print(f'MAIOR DISTÂNCIA = {dist3:.2f}')