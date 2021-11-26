'''

7. (Função com retorno sem parâmetro) Faça uma função/método retorne um vetor
com os três primeiros números perfeitos. Sabe-se que um número é perfieto
quando é igual a soma de seus divisores (exceto ele mesmo).

Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito.

'''

def perfeito():
  lista = []
  for x in range (1, 999, 1):
    soma = 0
    for z in range (1,x,1):
      if x % z == 0:
        soma = soma + z
    if soma == x:
      lista.append(x)
  return lista

lista = perfeito()
print(" Os Números ", lista,"são perfeitos ")


'''
# RESULTADO....

Os Números  [6, 28, 496] são perfeitos 

'''
