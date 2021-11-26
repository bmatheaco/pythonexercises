'''
9. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco
valores inteiros, determine e mostre o maior e o menor deles


'''

import numpy as np 

def valores(): #Declaração da função
      
    num = np.empty([5,1], dtype = int) 
    maior_n = 0
    menor_n = 0

    for lin in range(5):
      for col in range(1):
        num[lin,col]= float(input('Informe um número: '))
        
        if num[lin,col] > maior_n:
          maior_n = num[lin,col]
        
        else:
          menor_n = num[lin,col]
    print()
    print('O maior nº é: ',maior_n)
    print('O menor nº é: ',menor_n)

valores()


'''
# RESULTADO....

Informe um número: 8
Informe um número: 18
Informe um número: 3
Informe um número: 6
Informe um número: 2

O maior nº é:  18
O menor nº é:  2

'''
