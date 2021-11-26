
'''
(Função com retorno com parâmetro) Faça uma função/método que calcule
a média de um aluno que realizou duas provas (P1 e P2)e retorne a média,
a partir desta média, chame/crie OUTRA função que verifique se esta média
aprova ou reprova o aluno


'''

def status(m): #2º função
  if m >= 6:
    print('Aprovado')
  else:
    print ('Reprovado')

def media(a,b): #1º função
  m = (p1+p2)/2
  return(m) #chamada da função com return

#Chamada função principal
p1 = float(input('Informe sua nota na P1: ')) 
p2 = float(input('Informe sua nota na P2: '))
print('A Média é ',media(p1,p2))

status(media(p1,p2)) #chamada da 2ª função, após a primeira ser executada



