'''
Faça um programa que solicite ao usuário um valor decimal positivo (esse valor 
corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de 
cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$ 
0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.
'''

import sys

print('instruções: para inserir os valores corretamente siga o exemplo: 2519 = 25 Casa das centenas; 1 Casa das dezenas e 9 casa das unidades. Valor decimal = 0.XX')
print('Para calcular a quantidade de cedulas de um valor, informe seus agoritmos correspondentes a:')
valor_centenas = int(input('casa das centenas para cima:'))
valor_dezenas = int(input('casa das dezenas:'))
valor_unidades = int(input('casa das unidades: '))
valor_moedas = float(input('Insira o valor decimal:'))

if valor_centenas < 0:
    sys.exit('Não é um valor valido')
if 10 < valor_dezenas < 0:
    sys.exit('Não é um valor valido')
if 10 < valor_unidades < 0:
    sys.exit('Não é um valor valido')
if 0.99 > valor_moedas > 1:
    sys.exit('Não é um valor valido')

#calculo dos decimos

notas50 = 0
notas20 = 0
notas10 = 0
if valor_dezenas == 9:
    notas50 = 1
    notas20 = 2
elif valor_dezenas == 8:
    notas50 = 1
    notas20 = 1
    notas10 = 1
elif valor_dezenas == 7:
    notas50 = 1
    notas20 = 1
elif valor_dezenas == 6:
     notas50 = 1
     notas10 = 1
elif valor_dezenas == 5:
    notas50 = 1
elif valor_dezenas == 4:
    notas20 = 2
elif valor_dezenas == 3:
    notas20 = 1
    notas10 = 1
elif valor_dezenas == 2:
    notas20 = 1
else:
    notas10 = 1


#unidades
notas5 = 0
notas2 = 0
notas1 = 0
if valor_unidades == 9:
    notas5 = 1
    notas2 = 2
elif valor_unidades == 8:
    notas5 = 1
    notas2 = 1
    notas1 = 1
elif valor_unidades == 7:
    notas5 = 1
    notas2 = 1
elif valor_unidades == 6:
     notas5 = 1
     notas1 = 1
elif valor_unidades == 5:
    notas5 = 1
elif valor_unidades == 4:
    notas2 = 2
elif valor_unidades == 3:
    notas2 = 1
    notas1 = 1
elif valor_unidades == 2:
    notas2 = 1
else:
    notas1 = 1

#calculo moedas

moedas50 = 0.50
moedas25 = 0.25
moedas10 = 0.10
moedas5  = 0.5
moedas1  = 0.1


print(f'Valor em cedulas vai ser:\n 100 reais: {valor_centenas} \n 50 reais:{notas50} \n 20 reais:{notas20} \n 10 reais:{notas10} \n 5 reais:{notas5} \n 2 reais:{notas2}')
print(f'Valor em moedas vai ser: \n 1 real:{notas1} \n 50 centavos:{moedas50} \n 25 centavos:{moedas25} \n 10 centavos:{moedas10} \n 5 centavos:{moedas5} \n 1 centavos:{moedas1}')