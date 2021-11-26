'''
9. (Função com retorno sem parâmetro) Foi realizada uma pesquisa sobre algumas
características fisicas de cinco habitantes de uma região. Foram coletados os
seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino),
cor dos olhos (A - azuis ou C - castanhos),
cor dos cabelos (L - louros, P - pretos ou C - castanhos).

* Faça uma função/método que leia esses dados, armazenando-os em vetores(listas);

* Faça uma função/método que determine e devolva ao programa principal a média
de idades das pessoas com olhos castanhos e cabelos pretos.

* Faça uma função/método que determine e devolva ao programa principal a maior
idade entre os habitantes.

* Faça uma função/método que determine e devolva ao programa principal a
quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos
(inclusive) e que tenham olhos azuis e cabelos louros.

'''

idade = []
sexo = []
olhos = []
cabelos = []

def media_idade(): 
  cont = 0
  soma_idade = 0
  media = 0
  for x in range(5):
    if olhos[x].upper() == 'C' and cabelos[x].upper() == 'P':
      soma_idade = soma_idade + idade[x]
      cont = cont + 1
      media = soma_idade/cont
  return media 

def maior_idade():
  maior = 0
  for x in range(5):
    if idade[x] > maior:
      maior = idade[x]
  
  return maior

def qtd_fem():
  qtd = 0
  for x in range(5):
    if olhos[x].upper() == 'A' and cabelos[x].upper() == 'L':
      if idade[x] >= 18 and idade[x] <= 35:
        qtd = qtd + 1
  
  return qtd

def dados():
  for x in range(5):
    print('\n\nCaracterísticas do %dº habitante'%(x+1))
    idade.append(int(input('Digite a idade: ')))
    sexo.append(input('Digite o sexo (M - masculino ou F - feminino): '))
    olhos.append(input('Digite a cor dos olhos (A - azuis ou C - castanhos): '))
    cabelos.append(input('Digite a cor do cabelo (L - louros, P - pretos ou c - castanhos): '))

  print('\n\nA Média de idade de pessoas com Olhos Castanhos e Cabelos Pretos é: ', media_idade())
  print('A Maior idade entre os habitantes é: ', maior_idade())
  print('A Quantidade de mulheres com idade entre 18 e 35 anos, com Olhos Azuis e Cabelos Louros é: ', qtd_fem())

dados()
     
)

'''
# RESULTADO....



Características do 1º habitante
Digite a idade: 29
Digite o sexo (M - masculino ou F - feminino): F
Digite a cor dos olhos (A - azuis ou C - castanhos): A
Digite a cor do cabelo (L - louros, P - pretos ou c - castanhos): L


Características do 2º habitante
Digite a idade: 18
Digite o sexo (M - masculino ou F - feminino): F
Digite a cor dos olhos (A - azuis ou C - castanhos): C
Digite a cor do cabelo (L - louros, P - pretos ou c - castanhos): C


Características do 3º habitante
Digite a idade: 28
Digite o sexo (M - masculino ou F - feminino): M
Digite a cor dos olhos (A - azuis ou C - castanhos): A
Digite a cor do cabelo (L - louros, P - pretos ou c - castanhos): L


Características do 4º habitante
Digite a idade: 20
Digite o sexo (M - masculino ou F - feminino): M
Digite a cor dos olhos (A - azuis ou C - castanhos): A
Digite a cor do cabelo (L - louros, P - pretos ou c - castanhos): P


Características do 5º habitante
Digite a idade: 32
Digite o sexo (M - masculino ou F - feminino): F
Digite a cor dos olhos (A - azuis ou C - castanhos): C
Digite a cor do cabelo (L - louros, P - pretos ou c - castanhos): P


A Média de idade de pessoas com Olhos Castanhos e Cabelos Pretos é:  32.0
A Maior idade entre os habitantes é:  32
A Quantidade de mulheres com idade entre 18 e 35 anos, com Olhos Azuis e Cabelos Louros é:  2

'''
