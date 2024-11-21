'''
7. (Valor: 25 pontos) Desenvolva um código em Python que solicite ao usuário que informe os 
comprimentos dos três lados de um triângulo. Em seguida, verifique se esses comprimentos podem 
formar um triângulo. Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e classifique
o quanto aos lados e aos ângulos. 
• Instruções: 
a) Peça ao usuário para inserir os comprimentos dos três lados do triângulo. 
b) Verifique se os comprimentos fornecidos podem formar um triângulo. Caso contrário, informe 
que não é possível formar um triângulo com esses lados. 
c) Se for possível formar um triângulo, calcule os três ângulos do triângulo. 
d) Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) e aos ângulos 
(agudo, obtuso ou retângulo). 
e) Exiba a classificação do triângulo quanto aos lados e aos ângulos. 
• Observações: 
o Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, é necessário 
verificar a seguinte condição: A soma de quaisquer dois lados de um triângulo deve ser 
sempre maior que o terceiro lado. 
o Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo. 
o Para classificar quanto aos lados, verifique se os três lados são iguais (equilátero), se dois 
lados são iguais (isósceles) ou se todos os lados são diferentes (escaleno). 
o Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 90 graus 
(obtuso), se um dos ângulos é igual a 90 graus (retângulo) ou se todos os ângulos são 
menores que 90 graus (agudo). 
o Considere que os ângulos são expressos em graus. 
Desenvolva o código em Python para atender às especificações acima. 
Dica: Utilize a biblioteca math.
'''
#ler a biblioteca math, lei dos coscenos
import math 
import sys



ladoA = float(input('Digite o valor do lado A:'))
ladoB = float(input('Digite o valor do lado B:'))
ladoC = float(input('Digite o valor do lado C:'))

if ladoA > (ladoB + ladoC): 
    sys.exit('Não é um triangulo valido pelo teorema de existencia') 
elif ladoB > (ladoA + ladoC): 
    sys.exit('Não é um triangulo valido pelo teorema de existencia')    
elif ladoC > (ladoB + ladoA): 
    sys.exit('Não é um triangulo valido pelo teorema de existencia') 
#Preferi usar a lei dos cossenos
else: 
    print('é um triangulo valido pelo teorema de existencia')
    ang_a = math.acos((ladoA **2 - ladoB **2 - ladoC **2)/(-2*ladoB*ladoC))
    ang_b = math.acos((ladoB **2 - ladoA **2 - ladoC **2)/(-2*ladoA*ladoC))
    ang_c = math.acos((ladoC **2 - ladoB **2 - ladoA **2)/(-2*ladoB*ladoA))

    print(f'Os angulos são:\n{(180/math.pi)*ang_a: .2f} \n{(180/math.pi)*ang_b: .2f} \n{(180/math.pi)*ang_c: .2f}')

    #Para classificar os ângulos:

    if (ang_a or ang_b or ang_c) == (math.pi/2):
        print("Triângulo reto")
    elif ang_a > math.pi/2 or ang_b > math.pi/2 or ang_c > math.pi/2:
        print("Triângulo obtuso")
    else:
        print("Triângulo acutângulo")

    #Para classificar quanto aos lados:

    if (ladoA == ladoB) and (ladoB == ladoC):
        print("Equilátero") 
    elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
        print("Isósceles")
    else:
        # ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print("Escaleno")