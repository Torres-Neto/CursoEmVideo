'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele AINDA VAI SE ALISTAR ao serviço militar.
- Se é a HORA DE SE ALISTAR.
- Se já PASSOU DO TEMPO do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
sexo = input('Qual seu sexo [M] ou [F]? ')
if sexo == 'F' or sexo == 'f':
    print('Pessoas do sexo feminino não tem a obrigatoriedade de alistamento.')
else: 
    ano = int(input('Ano de nascimento: '))
    dataAtual = date.today().year
    idade = dataAtual - ano
    if idade > 0 and idade < 18:
        print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, dataAtual))
        print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format((18 - idade) + dataAtual))
    elif idade == 18:
        print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, dataAtual))
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade > 18:
        print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, dataAtual))
        print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
        print('Seu alistamento foi {}.'.format(dataAtual - (idade - 18)))
    else:
        print('Opção inválida! Tente Novamente!')