'''

10. (Função sem retorno sem parâmetro) Faça uma função/método que leia um
valor inteiro e positivo N e mostre o valor de S, obitod pelo seguinte cálculo:
S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!


'''

def valor():
  num  = int(input('Informe um número para calcular fatorial: '))
  s = 1 
  print(f'{num}!' , end=' ')

  for a in range(num, 0, -1):
      s *= a
      print( a,' x ' if a > 1 else ' = ' , end = ' ')
 
  print(s)


valor()


'''
# RESULTADO....

Informe um número para calcular fatorial: 3
3! 3  x  2  x  1  =  6

'''
