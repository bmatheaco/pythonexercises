'''

3. (Função com retorno sem parâmetro) Faça um programa contendo uma função/
método que leia a base e a altura de um triângulo e retorne/apresente sua
área (A = (base x altura)/2).

'''

def area():
  base = int(input("Informe o valor da base: "))
  altura = int(input("Informe o valor da altura: "))
  a = (base * altura)/2
  return a

#Chamada
print('Inicio')
print ('A Area = ', area())


'''
# RESULTADO....

Inicio
Informe o valor da base: 10
Informe o valor da altura: 12
A Area =  60.0

'''
