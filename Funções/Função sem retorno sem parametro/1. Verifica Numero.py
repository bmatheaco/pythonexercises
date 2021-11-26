'''
1. (Função sem retorno sem parâmetro) Faça um programa contendo uma função/método
que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.

'''



def verifica(): #DECLARAÇÃO DA FUNÇÃO
    a = int(input('Informe um número: '))
    if a > 0:
      print('1')
    else:
      print (0)

verifica () #CHAMADA FUNÇÃO


'''
# RESULTADO....

Informe um número: -7
0

'''
