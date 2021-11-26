'''

6. (Função com retorno sem parâmetro) Faça um programa contendo uma
função/método que verifique se um número é par, retorne/mostre o valor
booleano True para par e False para ímpar.

'''

def verifica():
  num = int(input("Informe um número: "))
  
  if num % 2 == 0:
    return True
  else:
    return False
  
#Armazene o conteúdo da função, em uma variavel e responda em portugues
#se é par ou impar 

x = (verifica())
if x == True:
  print('É Par')
else: 
  print('É Impar')


'''
# RESULTADO....

Informe um número: 3
É Impar

'''
