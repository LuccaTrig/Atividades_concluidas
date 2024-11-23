'''
Faça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a soma dos seus algarismos.
'''
import sys

numero = int(input('Insira um numero inteiro de até 4 digitos: '))

if numero < 0:sys.exit('Não é eum numero valido 1')

elif numero > 9999: sys.exit('Não é um numero valido 2')

milhar = numero // 1000
numeroCent = numero % 1000
centena = numeroCent // 100
opDecimal = numeroCent % 100
dezena = opDecimal // 10
unidade = opDecimal % 10 
somaAlgarismos = milhar + centena + dezena + unidade




print(f' Numero = {numero} milhar = {milhar} centena = {centena} Dezena = {dezena} unidade = {unidade} soma dos algarismos = {somaAlgarismos}')
