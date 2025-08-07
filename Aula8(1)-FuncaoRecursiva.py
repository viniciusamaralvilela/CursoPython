#aprendi com a ana leticia. É aquele função que chama ela mesmo

print ('Programa que calcula o fatorial')
print()

def fatorial(numero):
    if(numero <= 1): #tem que ter essa condição! Que nem na matematica, se eu não colocar isso vai dar erro pois vai somando infinitamente.
        return 1
    else:
        return numero * fatorial(numero - 1)

digitar = int(input('Digite um numero: '))
print(fatorial(digitar))