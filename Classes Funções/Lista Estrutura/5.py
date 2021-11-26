class Banco:
    numero = 0
    nome = ''
    saldo = 0

def cadastro(vetB):
    for i in range(2):
        banco = Banco()
        banco.numero = int(input('Informe o número da conta: '))
        banco.nome = input('Informe o nome: ')
        banco.saldo = float(input('Informe o saldo: '))
        vetB.append(banco)
    return vetB

def Visualizar(vetB):
    pesquisar = input('Informe o nome do cliente: ').upper()
    for i in range(len(vetB)):
        if pesquisar.upper() in vetB[i].nome.upper():
          print('Cliente: ',vetB[i].nome,'\nNúmero da Conta: ',vetB[i].numero,'\nSaldo: ', vetB[i].saldo)
          print('-'*50)

def Excluir(vetB):
    excluir = str(input('Deseja excluir a conta de menor saldo? (S ou N): ')).upper()
    if excluir == 'S':
        for i in range(len(vetB)):
          if i == 0:
            menor = vetB[i].saldo
            conta = i
            print('o resultado é: ',conta)
          else:
            if vetB[i].saldo < menor:
              menor = saldo
              conta = i
              print('o resultado é: ',conta)
        vetB.pop(conta)

def main():
    vetB = []
    op = 1
    while op >= 1 <=3:
      print('-'*50)
      print('1 - Cadastrar contas')
      print('2 - Visualizar todas as contas de um determinado cliente')
      print('3 - Excluir a conta com menor saldo')
      print('4 - Sair')
      print('-'*50)
      op = int(input('Digite a opção desejada: '))
      if op == 1:
        cadastro(vetB)
      elif op == 2:
        Visualizar(vetB)
      elif op == 3:
        Excluir(vetB)
      elif op == 4:
        print('......................Sistema Encerrado......................')
      else:
        print('......................Sistema Encerrado......................')
main()
