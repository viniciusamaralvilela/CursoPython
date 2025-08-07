#tratamento de erro visa me alertar o tipo de erro que ocorreu na aplicação. Banco de dados por exemplo

try: #ele tenta um código, se der errado:
    print('oi')
except: #chama o except
    print('Algo de errado')


else: #se não entrou no except, chama esse else pós try
    print('Deu tudo certo')
finally: #Ele não liga se deu erro ou não.
    print('Deu certo ou errado')

