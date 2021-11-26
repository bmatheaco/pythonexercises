class Endereco:
  logradouro = ''
  numero = 0
  bairro = 0

class Alunos:
  nome = ' '
  dia = 0
  mes = 0
  ano = 0
  telefone = 0
  endereco = Endereco()
  serie = 0
  ra = 0
def Cadastrar(vetA):
  print('******* CADASTRO DOS ALUNOS ******* ')
  for i in range(2):
    aluno = Alunos()
    aluno.nome = input('Informe o nome do aluno: ')
    aluno.ra = int(input('Informe o RA: '))
    aluno.dia = int(input('Informe dia: '))
    aluno.mes = int(input('Informe o mês: '))
    aluno.ano = int(input('Informe o ano: '))
    aluno.telefone = int(input('Informe o telefone: '))
    aluno.endereco.logradouro = input('Informe a sua rua: ')
    aluno.endereco.numero = int(input('Informe o número da casa: '))
    aluno.endereco.bairro = input('Informe o bairro: ')
    aluno.serie = input('Informe o numero da serie: ')
    vetA.append(aluno)
  return vetA


def Consultar(vetA):
  print('Consultar por nome...........')
  nomePesquisa = input('Pesquisar o aluno por nome: ')
  for i in range(2):
    if nomePesquisa == vetA[i].nome:
      print('********** CONSULTAR ********')
      print('RA: ', vetA[i].ra)
      print('Nome: ', vetA[i].nome)
      print('Data de nascimento: {}/{}/{}'.format(vetA[i].dia,vetA[i].mes,vetA[i].ano))
      print('Telefone: ', vetA[i].telefone)
      print('Endereço: ', vetA[i].endereco.logradouro)
      print('Numero: ', vetA[i].endereco.numero)
      print('Bairro: ', vetA[i].endereco.bairro)
      print('', vetA[i].serie,'ºsérie')


def Mostrar(vetA):
  for i in range(2):
    print('************** TABELA DE ALUNOS **************')
    print('RA: ', vetA[i].ra)
    print('Nome: ', vetA[i].nome)
    print('Data de nascimento: {}/{}/{}'.format(vetA[i].dia,vetA[i].mes,vetA[i].ano))
    print('Telefone: ', vetA[i].telefone)
    print('Endereço: ', vetA[i].endereco.logradouro)
    print('Numero: ', vetA[i].endereco.numero)
    print('Bairro: ', vetA[i].endereco.bairro)
    print('', vetA[i].serie,'ºsérie')

def Sair(vetA):
  for i in range(2):
    print('Codigo encerrado.')
    break

def main():
  op = 1
  while op >=1 and op <= 3:
    print('MENU DE GERENCIAMENTO')
    print('1 - Cadastrar')
    print('2 - Mostrar')
    print('3 - Consultar')
    print('0 - Sair')
    op = int(input('Digite a opção:'))
    if op == 1:
      vetA = []
      vetA = Cadastrar(vetA)
    elif op == 2:
      Mostrar(vetA) 
    elif op == 3:
      Consultar(vetA)
    elif op == 0:
      Sair(vetA)
    
 
main()
