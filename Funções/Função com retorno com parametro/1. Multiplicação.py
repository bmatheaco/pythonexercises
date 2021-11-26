'''
1. (Função com retorno com parâmetro) Faça um programa contendo uma
função/método que receba por parâmetro um número e o multiplique por 2,
retorne e apresente o resultado da função.

'''

#declaração da função
def multiplica(b):
    w = b * 2
    return w

#chamada da função pelo print, MAS AGORA TEM PASSAGEM DE PARÂMETRO
num = int(input('Informe um número '))
print('O resultado é', multiplica(num)  )
#ou....................
f = multiplica(num)
print('O resultado é', f )



'''
RESULTADO:

Informe um número 5
O resultado é 10
O resultado é 10

'''
