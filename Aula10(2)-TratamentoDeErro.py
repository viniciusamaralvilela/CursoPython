#não tem como dividr por zero
print('Programa de divisão de numeros')
print()

try:
    numero = float(input('Digite um número: '))
    divisor = float(input('Digite um divisor para o numero: '))
    resultado = numero / divisor
    print(resultado)
except: 
    print('Você digitou algo errado')
    print('Verifique se digitou um numero pertencente o conjunto dos REAIS, ou se tentou dividir por zero')

#TODOS OS BLOCOS QUE ESTIVER FORA DO TRY NÃO FUNCIONA CORRETAMENTE. 