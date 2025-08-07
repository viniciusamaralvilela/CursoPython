#classe filha herdando atributos da principal
#exemplo da ave
#exemplo com smart watch
#a classe filha não pode ficar vazia. Mas posso criar uma função própria dela, ou ate mesmo uma variavel, só que o declarado no _init_ é o mesmo

class Smartphone:
    def __init__(self,marca,modelo,cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def ligar(self):
        print('TRUMMMMMMMMMMMMMM')

print('------------------------------')
print()

class Smartwatch(Smartphone): #classe filha herdando a estrutura da classe mãe
    batimento = True
    def status(self):
        print('Verificando batimentos...')

mar = input('Digite a marca: ')
mod = input('Digite o modelo: ')
c = input('Digite a cor: ')
relogio1 = Smartwatch(mar, mod, c)
print('Marca: ',relogio1.marca)
print('Modelo: ',relogio1.modelo)
print('Cor: ',relogio1.cor)
print('Batimento: ', relogio1.batimento)
print(relogio1.status())
