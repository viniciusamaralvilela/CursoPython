#IA trabalha com dataset's
#aqui vamos ver como funciona um 
#esses arquivos contém dados em que podemos fazer previsões. Vamos ler esses arquivos aqui.
#Tem que ser arquivo .csv

print('Previsão de arquivos')
print('---------------------')

import pandas #analise e manipulação de dados, especialmente planilhas
from sklearn import linear_model #previsao

colunas = pandas.read_csv('Valores.csv')
dia = colunas[['Dia']].values #pegando os valores de dia pra não ficar dando mensagem de erro
valor = colunas['Valor']

calculo = linear_model.LinearRegression()
calculo.fit(dia, valor) #aqui eu busco o padrao a partir de dia e valor

data = int(input('Digite o dia da previsão: '))
previsao = calculo.predict([[data]]) #buscar o dia 10 atraves do padrao
print('A previsão é: ', previsao)

