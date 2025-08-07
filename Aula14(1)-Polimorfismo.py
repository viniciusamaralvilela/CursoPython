#mesma função em classes maes e filhas 

class Smartphone:
    def __init__(self,marca,modelo,cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def ligar(self):
        print('TRUMMMMMMMMMMMMMM')
    
    def despertar(self):
        print('Despertador do celular ativado')

print('------------------------------')
print()

class Smartwatch(Smartphone): 
    def __init__(self, marca, modelo, cor, batimento): #copia o da classe mãe, e adiciona no final o atributo que voce quer passar
        super().__init__(marca, modelo, cor) #esse super "recicla" o que já está declarado na classe mae e vc quer reutilizar
        self.batimento = batimento #add o batimento, como la em cima
    def status(self):
        print('Verificando batimentos...')
    def despertar(self):
        print('Despertador do relógio ativado')

mar = input('Digite a marca: ')
mod = input('Digite o modelo: ')
c = input('Digite a cor: ')
bat = input ('Digite o batimento: ')
relogio1 = Smartwatch(mar, mod, c, bat)
print('Marca: ',relogio1.marca)
print('Modelo: ',relogio1.modelo)
print('Cor: ',relogio1.cor)
print('Batimento: ', relogio1.batimento)
print(relogio1.status())
print(relogio1.despertar()) #declarar o objeto para chamar certinho

celular1 = Smartphone('Apple', "Iphone SE", "Azul")
print(celular1.marca)
print(celular1.modelo)
print(celular1.cor)
print(celular1.despertar())
