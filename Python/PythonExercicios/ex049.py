'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.
'''
n = int(input('Digite um número qualquer: '))
print('>>>>>>>>>>>>>>>')
print('Tabuada de ',n)
for i in range(1, 10+1):
    print('{:2}  x {:2} = {:2}'.format(n, i, n*i))
print('>>>>>>>>>>>>>>>')