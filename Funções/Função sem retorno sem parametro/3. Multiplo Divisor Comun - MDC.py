'''
3. (Função sem retorno sem parâmetro) Faça uma função/método que receba três
números inteiros a, b, c que sejam divisíveis por a (inclusive b e c) e apresente a quantidade e os números divisíveis.

Exemplo:
    a = 5
    b = 1
    c = 10
    qtde = 2
'''

def divisores():
  a = int(input('1-Informe um número: '))
  b = int(input('2-Informe um número: '))
  c = int(input('3-Informe um número: ')) 
  cont=0
  
  for b in range (b,c+1):
    if b % a == 0:
      cont += 1
    
  print('Nº ',cont, 'é o divisor comum')


divisores()



'''
# RESULTADO....

1-Informe um número: 5
2-Informe um número: 1
3-Informe um número: 10
Nº  2 é o divisor comum

'''
