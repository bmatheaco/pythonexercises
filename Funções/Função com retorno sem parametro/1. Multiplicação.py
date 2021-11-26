'''

1. (Função com retorno sem parâmetro) Faça um programa contendo uma
função/método que leia um número e o multiplique por 2 retornando o resultado,
apresente o resultado da função.

'''

#declaração da função
def multiplica():
    num = int(input('Informe um número '))
    w = num * 2
    return w

#chamada da função
multiplica() 
#ou
f = multiplica()
print('O resultado é', f )
#ou 
print('O resultado é', multiplica()  )

'''
# RESULTADO....

Informe um número 5
Informe um número 5
O resultado é 10
Informe um número 5
O resultado é 10

'''
