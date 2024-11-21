'''Questão 4'''
from datetime import datetime

diaInicial = int(input('Inserir dia inicial:'))
mesInicial = int(input('Inserir mês inicial:'))
diaFinal   = int(input('Inserir dia final:'))
mesFinal   = int(input('Inserir mês final:'))
#Ano incial do datetime
ano_epoch = 1970


date_inicial = datetime(ano_epoch, mesInicial, diaInicial)
date_final= datetime(ano_epoch, mesFinal, diaFinal)

if date_inicial > date_final:
    print("Datas invalidas")

else:

    segundos_I= int(date_inicial.timestamp())
    segundos_F= int(date_final.timestamp())
    segundos_dia = (60*60*24)

    print(f'{(segundos_F - segundos_I)/segundos_dia}')
