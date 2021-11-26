'''

6. (Função sem retorno com parâmetro) Faça uma função/método para a partir
de um valor inicial e um valor final realizar o acumulo desse valores e
apresentar o resultado.

Exemplo:
    a = 2
    b = 8
    // 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
    r = 35

'''

def acum(x, y):
  if y <= x:
    print('ERRO')
  else:
    s = 0
    while x <= y:
      s += x
      x += 1
    print('O acúmulo dos valores entre esses números é igual a', s)

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
acum(a, b)

'''
# RESULTADO....

Primeiro valor: 2
Segundo valor: 8
O acúmulo dos valores entre esses números é igual a 35

'''
