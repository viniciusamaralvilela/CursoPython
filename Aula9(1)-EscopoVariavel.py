print('Programa de escopo')
print()

def exibir():
    profissao = 'Professor'
    nome = 'Elvis'
    return nome + ' ' + profissao

#print(profissao) não funciona pois é local da função exibir. Ou seja, ela nao "existe"
print(exibir())
idade = 45
print (idade)