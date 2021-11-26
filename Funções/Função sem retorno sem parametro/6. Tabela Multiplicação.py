'''
6. (Função sem retorno sem parâmetro) Faça uma função/método
que leia um valor inteiro entre e 9 e mostre a seguinte tabela de
multiplicação

Exemplo:

1    
2     4
3     6     9
4     8    12    16
5    10    15    20    25
6    12    18    24    30    36
7    14    21    28    35    42    49
8    16    24    32    40    48    56    64   
9    18    27    36    45    54    63    72    81
for i = 1 até n
   for j = 1 até i

'''
import numpy as np #importa matriz

def multiplica():
  n = int(input('Informe um número inteiro entre 1 e 9: ')) #indica nº de linhas

  tab = np.empty([n,n]) #Cria a matriz vazia, de n linhas e n colunas

  for linha in range (n):
    for coluna in range (n):
      tab[linha,coluna] = (1 + linha) * (1 + coluna)
  
  for linha in range (n):
    for coluna in range (n):
      if linha >= coluna:
       print('{0:.0f}   '.format( tab[linha,coluna]), end="" )
    print('\n') #Linha em branco para separar as linhas da coluna

multiplica() #chamada da função




'''
# RESULTADO....

Informe um número inteiro entre 1 e 9: 9
1   

2   4   

3   6   9   

4   8   12   16   

5   10   15   20   25   

6   12   18   24   30   36   

7   14   21   28   35   42   49   

8   16   24   32   40   48   56   64   

9   18   27   36   45   54   63   72   81   



'''
