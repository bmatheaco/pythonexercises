'''

7. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro,
para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se
o valor é par ou ímpar.

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

Informe um número: 21
21
impar

'''
