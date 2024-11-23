
import datetime as dt #importanto a bib 'datetime' com o apelido 'dt', assim eu posso chamar por ela apenas com o 'dt'


genero = input("Informe o seu sexo.\n\"M\" para masculino ou \"F\" para feminino: ")
nascimento_input = input("Informe sua data de nascimento (formato DD/MM/AAAA): ")
contribuicao_input = input("Informe a data de ínicio da sua contribuição com a previdência (formato DD/MM/AAAA): ")


data_nascimento = dt.datetime.strptime(nascimento_input, "%d/%m/%Y") #transformando no formato dia/mês/ano
data_contribuicao = dt.datetime.strptime(contribuicao_input, "%d/%m/%Y") 
data_atual = dt.datetime.now() 

idade = (data_atual - data_nascimento).days//365 #cálculo para contabilizar a idade (em anos)
contribuicao = (data_atual - data_contribuicao).days//365 #cálculo para contabilizar o tempo de contribuição (em anos)

if genero == 'M':

    if idade >= 65 and contribuicao >= 15:
        print("Você pode se aposentar devido a idade")
    elif idade >= 65:
        print(f"Você pode se aposentar em: {15 - contribuicao} anos")
    elif (65 - idade) < (15 - contribuicao):
        print(f"Você pode se aposentar em: {(62-idade)+(15 - contribuicao)} anos")
    elif (65 - idade) < (35-contribuicao):
        print(f"Você pode se aposentar em: {(65-idade)+(35 - contribuicao)} anos")
    elif contribuicao >= 35:
        print("Você pode se aposentar devido o tempo de contribuição")
else:

    if idade >= 62 and contribuicao >= 15:
        print("Você pode se aposentar devido a idade")
    elif idade >= 62:
        print(f"Você pode se aposentar em: {15 - contribuicao} anos")
    elif (62 - idade) < (15 - contribuicao):
        print(f"Você pode se aposentar em: {(62-idade)+(15 - contribuicao)} anos")
    elif (62 - idade) < (30-contribuicao):
        print(f"Você pode se aposentar em: {(62-idade)+(30 - contribuicao)} anos")
    elif contribuicao >= 30:
        print("Você pode se aposentar devido o tempo de contribuição")
