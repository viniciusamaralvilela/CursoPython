#def é responsavel por criar a função
#segue uma ordem sequencial. Ou seja, declarar a função antes e DEPOIS enviar um parãmetro por exemplo
#parametro e retorno

print('Programa que calcula o dobro usando funções')
print()
def dobro(valor):
    return valor * 2

numero = int(input('Digite o número: '))
print(dobro(numero))