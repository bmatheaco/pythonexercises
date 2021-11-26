'''

2. (Função sem retorno com parâmetro) Faça um programa
contendo uma função/método para subtrair dois números e apresentar o resultado.

'''

def status(m): #2º função
  if m >= 6:
    print('Aprovado')
  else:
    print ('Reprovado')

def media(a,b): #1º função
  m = (p1+p2)/2
  print('Sua Média é: ',m)
  status(m) #chamada 2º função, chamada após a primeira ser executada


p1 = int(input('Informe sua nota na P1: '))
p2 = int(input('Informe sua nota na P2: '))
media(p1,p2) 

'''
# RESULTADO....

Informe sua nota na P1: 8
Informe sua nota na P2: 10
Sua Média é:  9.0
Aprovado

'''
