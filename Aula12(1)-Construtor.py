#construir a classe
#funcao especial que inicializa os argumentos da classe
#self = eu mesmo, esse objeto aqui

class Smartphone:
    def __init__(self,marca,modelo,cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def ligar(self):
        print('TRUMMMMMMMMMMMMMM')

print('------------------------------')
print()

mar = input('Digite a marca: ')
mod = input('Digite o modelo: ')
c = input('Digite a cor: ')
celular1 = Smartphone(mar, mod, c)
print('Marca: ',celular1.marca)
print('Modelo: ',celular1.modelo)
print('Cor: ',celular1.cor)

print('---------------------------------------')
celular1.ligar()