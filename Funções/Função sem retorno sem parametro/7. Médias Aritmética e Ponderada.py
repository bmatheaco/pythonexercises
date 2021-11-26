'''
7. (Função sem retorno sem parâmetro) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética das notas dos alunos, se for P,
deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada.


'''
def nota():
  print('Informe de acordo: A para Média Aritimética ou P Média Ponderada')
  print('\n')

  m = input('Digite a opção escolhida: ')
  n1 = float(input('Informe Nota 1: '))
  n2 = float(input('Informe Nota 2: '))
  n3 = float(input('Informe Nota 3: '))

  if m == 'A' or m == 'a':
    media = (n1 + n2 + n3) / 3
    print('Sua Média Aritimética é: ',media)
  
  else:
    media = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
    print('Sua Média Ponderada é: ',media)

nota()


'''
# RESULTADO....

Informe de acordo: A para Média Aritimética ou P Média Ponderada


Digite a opção escolhida: P
Informe Nota 1: 6
Informe Nota 2: 3
Informe Nota 3: 1
Sua Média Ponderada é:  4.1

'''
