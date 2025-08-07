#orientada a objetos

class Smartphone:
    marca = 'Apple'
    modelo = 'Iphone 14'
    cor = 'Black'
    
    def email(acao):
        print('Enviando um email...')
    def ligar (acao2):
        print('Ligando...')

print('Programa de classe')
print()

celular1 = Smartphone() # o celular um é do tipo smartphone, ou seja, celular1 é um iphone 14
print("Marca: ", celular1.marca)
print("Modelo: ", celular1.modelo)
print("Cor: ", celular1.cor)
print()
celular1.email()
print('---------------------------------------------')

celular2 = Smartphone()
celular2.marca = input('Digite a marca: ')
celular2.modelo = input('Digite o modelo: ')
celular2.cor = input('Digite a cor: ')

print("Marca: ", celular2.marca)
print("Modelo: ", celular2.modelo)
print("Cor: ", celular2.cor)