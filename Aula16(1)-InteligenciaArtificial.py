#pega dados e consegue extrair padrões através de expressões matematicas, e faz previsões

print('Programa de detecção de anomalia na compra')
print("------------------------------------------")
import numpy
from sklearn import linear_model 

valores = numpy.array([1400,2600,2100,1900,2000,3200,1780,4100]).reshape(-1, 1) 
#o reshape serve para separar os dados em linhas. Se for tudo agrupado, não é possivel que a biblioteca realize a previsao, pois ela espera entradas como matriz 2D

bloqueio = numpy.array([0, 0, 0, 0, 0, 1, 0, 1])
#nao preciso usar aqui pois ele representa saidas

modelo = linear_model.LogisticRegression() 
#função matematica que vou usar para fazer o calculo

modelo.fit(valores, bloqueio) 
#cria uma matriz


compra = float(input('Digite o valor da compra que deseja: '))
previsao = modelo.predict(numpy.array([compra]).reshape(-1, 1))
#compara o valor que quer buscar

if(previsao == 1):
    print('Está um valor alto')
else:
    print('Pode gastar')