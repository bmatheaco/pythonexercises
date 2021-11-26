'''

4. (Função com retorno sem parâmetro) Faça um programa contendo uma
função/método que leia o lado de um quadrado e retorne sua área (A = lado2).

Observação o número 2 significa ao quadrado.

'''

def quadrado():
  base = int(input("Informe o valor da base: "))
  a = base ** 2
  return a

#Chamada
print('Inicio')
print ('A Area = ', quadrado())

'''
# RESULTADO....

Inicio
Informe o valor da base: 2
A Area =  4

'''
