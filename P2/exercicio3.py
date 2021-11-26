class conta:
  numeroDaConta = 0
  nomeDoCliente = ' '
  saldo = 0,0


def Excluir(vetConta):
  print('~~Exclusão dos dados do cliente com menor saldo~~')
  for cliente in vetConta:
    if min(cliente.saldo):
      print('Numero da conta: {} \tNome do cliente: {} \tSaldo da conta: R$ {:.2f}'.format(cliente.numeroDaConta, 
                                                                                           cliente.nomeDoCliente, 
                                                                                           cliente.saldo))


def Visualizar(vetConta):
  print('~~Consulta por nome~~')
  nomePesquisa = input('Qual nome quer pesquisar? ')
  for cliente in vetConta:
    if nomePesquisa == cliente.nomeDoCliente:
      print('Numero da conta: {} \tNome do cliente: {} \tSaldo da conta: R$ {:.2f}'.format(cliente.numeroDaConta, 
                                                                                           cliente.nomeDoCliente, 
                                                                                           cliente.saldo))
    else:
      print('Esta pessoa não possui uma conta ou está digitado errado.')


def Cadastrar(vetConta):
  c = 1
  while c > 0 and c <= 15:
    a = conta()
    print('~~Cadastro de contas~~')
    a.numeroDaConta = int(input('Digite o número da conta (Digite \'0\' para sair): '))
    if a.numeroDaConta == 0:
      break
    a.nomeDoCliente = str(input('Digite o nome do cliente: '))
    a.saldo =float(input('Digite o saldo da conta: '))
    c += 1
    vetConta.append(a)
    print('Numero da conta: {} \tNome do cliente: {} \tSaldo da conta: R$ {:.2f}'.format(a.numeroDaConta, a.nomeDoCliente, a.saldo))
  return vetConta


def Menu():
  op = 1
  while op >=1 and op <= 3:
    print("~~Menu de Opções~~")
    print("   1. Cadastrar Contas.")
    print("   2. Visualizar todas as contas de um cliente.")
    print("   3. Excluir a conta com menor saldo.")
    print("   4. Sair.")
    op = int(input('Digite a opção: '))
    if op == 1:
      vetC = []
      vetC = Cadastrar(vetC)
    elif op == 2:
      Visualizar(vetC)
    elif op == 3:
      Excluir(vetC)


Menu()