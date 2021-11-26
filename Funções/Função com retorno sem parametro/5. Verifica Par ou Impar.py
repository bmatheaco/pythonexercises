'''

5. (Função com retorno sem parâmetro) Faça um programa contendo uma
função/método que verifique se um número é par, retorne mostrando a
str/string ‘É par’ ou se ‘É ímpar’.

'''

def verifica():
  num = int(input("Informe um número: "))
  x = num 
  if x % 2 == 0:
    return ('É Par')
  else:
    return ('É Impar')
  

print (verifica())


'''
# RESULTADO....

Informe um número: 3
É Impar

'''
