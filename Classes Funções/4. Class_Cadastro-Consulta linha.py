
'''
4.  Uma escola precisa montar o cadastro geral de seus alunos.
Este cadastro deverá conter os seguintes dados por aluno:
nome completo,
data de nascimento,
telefone,
endereço completo e
série atual.
Levando em conta que esta escola possui no máximo 500 alunos,
utilize estrutura para o sistema de controle, para cadastrar,
apresentar e consultar os alunos. Utilize funções.

'''    



class alunos:
  matricula = 0
  nome = ''
  dataN = ''
  telefone = 0
  endereco = ''
  serie = 0


def main():
  while True:
    print('.........................')
    print('Menu de Gerenciamento')
    print('1- Cadastrar')
    print('2- Consultar')
    print('3- Mostrar')
    print('4- Sair')
    opcao = int(input('O que deseja fazer? '))
    if opcao == 1:
      global listaAlunos
      listaAlunos = []
      listaAlunos = cadastrar(listaAlunos)
    elif opcao == 2:
      consultar(listaAlunos)
    elif opcao == 3:
      mostrar(listaAlunos)
    else:
      break


def cadastrar(listaAlunos):
  print('\n\nCadastro de alunos.........................')
  global c
  c = 0
  for i in range (500):
    if c == 0:
      a = alunos()
      a.matricula = int(input('\nMatrícula: '))
      a.nome = input('Nome completo: ')
      print('.........................')
      a.dataN = input('(Ex: 00/00/0000)\nData de Nascimento: ')
      print('.........................')
      a.telefone = int(input('Telefone: '))
      a.endereco = input('Endereço: ')
      a.serie = int(input('Série: '))
      print('.........................')
      listaAlunos.append(a)
      c += 1
    else:
      continuar = int(input('CONTINUAR?\n 1 - Sim\n 2 - Não: '))
      if continuar == 1:
        a = alunos()
        a.matricula = int(input('\nMatrícula: '))
        a.nome = input('Nome completo: ')
        print('.........................')
        a.dataN = input('(Ex: 00/00/0000)\nData de Nascimento: ')
        print('.........................')
        a.telefone = int(input('Telefone: '))
        a.endereco = input('Endereço: ')
        a.serie = int(input('Série: '))
        print('.........................')
        listaAlunos.append(a)
        c += 1
      elif continuar == 2:
        break
      else:
        print('COMANDO INVÁLIDO')
  return listaAlunos


def consultar(listaAlunos):
  print('\n\nConsulta por nome..........................')
  nomeConsulta = input('\nNome a ser consultado: ')
  semResultado = 0
  for i in range (c):
    if nomeConsulta == listaAlunos[i].nome:
      print('\nMatrícula: {0}\nNome: {1}\nData de Nascimento: {2}\nTelefone: {3}\nEndereço: {4}\nSérie: {5}'.format(listaAlunos[i].matricula, listaAlunos[i].nome, listaAlunos[i].dataN, listaAlunos[i].telefone, listaAlunos[i].endereco, listaAlunos[i].serie))
      print('.........................')
    else:
      semResultado += 1
  if semResultado == c:
    print('Nenhum resultado obtido')


def mostrar(listaAlunos):
  print('\n\nApresentaçao dos dados dos alunos..........')
  for i in range (c):
    print('\nMatrícula: {0}\nNome: {1}\nData de Nascimento: {2}\nTelefone: {3}\nEndereço: {4}\nSérie: {5}'.format(listaAlunos[i].matricula, listaAlunos[i].nome, listaAlunos[i].dataN, listaAlunos[i].telefone, listaAlunos[i].endereco, listaAlunos[i].serie))


main()
