class produto:
  codigo = 0
  nome = ''
  preco = 0.0
  aumento = 0.0

def aumento10(x):
    aumento = x + (x * 0.1)
    return aumento

def cadastrar5():
  vetp = []
  for i in range(5):
    a = produto()
    a.codigo = int(input('Qual o código: '))
    a.nome = input('Qual o nome: ')
    a.preco = float(input('Qual o preço: '))
    a.aumento = aumento10(a.preco)
    vetp.append(a)


  for i in range(5):
    print('\nCódigo:',vetp[i].codigo, '\nNome:', vetp[i].nome, '\nPreço: R$', vetp[i].preco, '\nPreço com 10% de aumento: R$', vetp[i].aumento)

cadastrar5()
