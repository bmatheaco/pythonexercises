'''
6. (Função com retorno com parâmetro) Faça um programa contendo uma
função/método que receba duas notas (P1, P2) calcule a média, chame
outra função que avalie se este aluno esta aprovado ou reprovado retornando
a str/string 'Aprovado' ou 'Reprovado'.

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

RESULTADO:

Informe sua nota na P1: 8
Informe sua nota na P2: 9
Sua Média é:  8.5
Aprovado


'''
