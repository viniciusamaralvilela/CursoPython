print('Calcular media')
print()
nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))
nota3 = float(input('Digite a terceira nota '))

media = (nota1 + nota2 + nota3)/3
print(media)

if media > 69:
    print('O aluno passou')
else:
    print('O aluno nao passou')