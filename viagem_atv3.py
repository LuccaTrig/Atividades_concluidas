'''
Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo. 
Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada 
(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto 
(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km);  
Após receber os dados, o programa informa dados típicos de um computador de bordo:  
a) o tempo de viagem (em segundos) 
b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h) 
c) o custo da viagem com combustível (em R$) 
d) o desempenho do carro (em Km/l, l/h e R$/Km).

Notas:
timedelta é usada para comparação de datas/hora: Calcular a diferença entre dois eventos, como o tempo entre o início e o fim de uma tarefa.
Também para Adição ou subtração de tempo: Se você quiser adicionar ou subtrair dias, horas ou minutos de uma data.


'''

from datetime import datetime, timedelta, time

#Questão A
tempo_inicial = input('Digite a hora de início (formato HH:MM): ')
tempo_final = input('Digite a hora de fim (formato HH:MM): ')
segundos_descanso = int(input('Inserir os segundos de descanso:'))

#formatação do tempo de viagem
formato_hora = '%H:%M'  
tempo_inicial_dt = datetime.strptime(tempo_inicial, formato_hora)
tempo_final_dt = datetime.strptime(tempo_final, formato_hora)

if tempo_final_dt < tempo_inicial_dt:
    tempo_final_dt += timedelta(days=1)

#formatação tempo de descanso
tempo_descanso_td = timedelta(seconds=segundos_descanso)

#calculo dos segundos
duracao = (tempo_final_dt - tempo_inicial_dt) - tempo_descanso_td
duracao_segundos = duracao.total_seconds()

print(f'A duração da viagem em segundos é: {duracao_segundos} segundos.')

#Questão B

distacia_viagem = int(input('Distância percorrida em Km:'))

horas_descanso =  duracao_segundos / 36000 #Tempo de viagem na estrada 
horas_totais = duracao_segundos + segundos_descanso #tempo total do ponto de partida até o destino(contando o descanso)
media_global = distacia_viagem / horas_descanso
media_movimento = distacia_viagem / horas_totais
print(f'A media global em Km/h é:{media_global:.2f} \n A media de movimento em km/h:{media_movimento:.2f}')

#Questão C

combustivel = float(input('Litros gastos durante a viagem:'))
combustivel_valor = float(input('Preço do combustível:'))

Total_combustivel = combustivel * combustivel_valor
print(f'O custo da viagem em combustivel foi: {Total_combustivel:.2f}') 

#Questão D : O desempenho do carro (em Km/l, l/h e R$/Km)

desempenho_kl= distacia_viagem / combustivel
desempenho_lh = combustivel / horas_descanso
desempenho_rk = Total_combustivel / distacia_viagem

print(f'O desempenho do carro em: \n Kilometro por litro é:{desempenho_kl:.2f} \n litros por horas é:{desempenho_lh:.2f} \n Reais por kilometro:{desempenho_rk:.2f}')