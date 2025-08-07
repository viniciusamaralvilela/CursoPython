#vetor em python é uma lista.

roupas = ['camisas', 'vestido', 'bermuda', 'calça']

for pecas in roupas : #percorrer a lista
    print(pecas)
print()

procura = input('Digite uma peça de roupa que deseja: ')
if procura in roupas: #verificar se existe algo dentro da lista
    print('encontrado')
else:
    print('Não encontrado')
print()
 
roupas.append('Luvas') #Adiconar um elemento na ultima posição
for pecas in roupas : #percorrer a lista
    print(pecas)
print()

roupas.remove('Luvas') #remover
for pecas in roupas : #percorrer a lista
    print(pecas)
print()

roupas.sort() #ordem alfabetica ou numerica
for pecas in roupas : #percorrer a lista
    print(pecas)
print()

roupas[1] = 'Jaqueta' #add algo em um indice escolhido
for pecas in roupas : #percorrer a lista
    print(pecas)
print()

Numeros = [10, 20, 10, 10, 10] #Lista aceita numeros, e tambem numeros com outros tipos primitivos, como char por exemplo
soma = sum(Numeros) #comando para somar tudo da lista. sum é um comando de soma
print(soma)
print()

Numeros = [10, 20, 10, 10, 10] 
maximo = max(Numeros) #comando para ver o maior valor da lista. Tem do minimo, que é min
print(maximo)
print()

roupas = ('camisas', 'Balcao') #É uma tupla, ela nao pode ser alterada. Serve so para mostrar