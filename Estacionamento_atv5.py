'''Questão 5

 Em um estacionamento, as tarifas são as seguintes (cumulativas): 
• Até duas horas: R$ 8,00/hora ou fração; 
• Entre três e quatro horas: R$ 5,00/hora ou fração; 
• Horas seguintes: R$ 3,00/hora ou fração. 
• Depois de 12h, o custo passa a ser fixo: R$ 30,00 
Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba 
o valor a ser pago pelo responsável. 
Como exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00 (pelas 
duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 (pela quinta hora e fração da 
sexta hora): total de R$ 32,00

'''

import math

min_estacionados = int(input('Minutos estacionados:'))
valor_total = 0
horas = math.ceil(min_estacionados / 60) 
print(f'horas:{horas}')
hrs2 = 16
hrs4 = 10
hrs12 = 24

if horas <= 2:
    valor_total = hrs2

elif horas <= 4: 
    horas= horas - 2
    valor_total = hrs2 + (horas * 5)

elif horas < 12:
    horas = horas - 4
    valor_total = hrs2 + hrs4 + (horas * 3)

elif horas >= 12:
    valor_total = hrs2 + hrs4 + hrs12 + 30

print(f'Total a pagar: {valor_total}')
