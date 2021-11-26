'''

9. (Função sem retorno com parâmetro) Faça uma função/método para verificar
se um nome digitado é igual a ‘Ana’, mostre o valor true ou false como resposta.

'''

def verifica(n): #2º função
  if x == 'ana' or x == 'Ana':
    print('True')
  else:
    print('False')


def nome(n): #1º função
  n = n
  print(n)

  verifica(n) #chamada 2º função, chamada após a primeira ser executada

x = input('Qual seu nome? ') 
nome(x)

'''
# RESULTADO....

Qual seu nome? Ana
Ana
True

'''
