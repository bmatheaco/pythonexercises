'''(Funçao sem retorno com parametro) faça um programa contendo uma
funçao/metodo que apresente se o numero for positivo ou negativo.'''

def verif(a):
    if a > 0:
        print('1')
    else:
        print('0')
        
a = int(input('Informe um numero: '))
verif(a)
