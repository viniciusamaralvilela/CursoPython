print('Programa de desconto')
print()
menu = 'yes'

while menu == 'yes':
    valor = float(input('Digite um valor: '))
    percentual = float(input("Digite um porcentual: "))/100
    resultado = valor * percentual
    
    print('O desconto é de: ', resultado)
    print('Você vai pagar: ', valor - resultado)
    menu = input('Digite yes or no, para prosseguir ou não: ')
    print()