print('Contar Pares')
print('')

print('Quantos numeros deseja digitar? ')
quant = int(input())

print('Digite os numeros agora')
contPar = 0;
for cont in range(quant):
    num = int(input())
    if num % 2 == 0:
        contPar += 1
print(contPar, 'são números pares')
    