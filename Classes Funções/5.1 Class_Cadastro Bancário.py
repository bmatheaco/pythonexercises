'''

5. Faça um programa que realize o cadastro de contas bancarias com as seguintes

informações: numero da conta, nome do cliente e saldo.

O banco permitirá o cadastramento de 15 contas.
Para cada opção crie uma função, inclusive uma
para mostrar o menu e obter a escolha do usuário para, assim, chamar as outras
funções. Crie o menu de opções a seguir:

Menu de opções:

Cadastrar contas
Visualizar todas as contas de um determinado cliente
Excluir a conta com menor saldo
Sair

'''




class contas:
    numConta = 0
    nomeCliente = ''
    saldo = 0.0


def main():
  while True:
    print('.........................')
    print('Menu')
    print('1- Cadastrar')
    print('2- Consultar contas em um mesmo nome')
    print('3- Excluir conta de menor saldo')
    print('4- Sair')
    op = int(input('O que deseja fazer? '))
    if op == 1:
      clientes = []
      clientes = cadastrar(clientes)
    elif op == 2:
      consultar(clientes)
    elif op == 3:
      excluir(clientes)
    else:
      break


def cadastrar(clientes):
    print('\n\nCadastro de clientes.........................')
    c = 0
    for i in range (15):
        if c == 0:
            a = contas()
            a.numConta = int(input('\nNúmero da conta: '))
            a.nomeCliente = input('Nome do cliente: ')
            a.saldo = float(input('Saldo em conta: R$'))
            print('.........................')
            clientes.append(a)
            c += 1
        else:
            continuar = int(input('CADASTRAR OUTRA CONTA?\n 1 - Sim\n 2 - Não: '))
            if continuar == 1:
                a = contas()
                a.numConta = int(input('\nNúmero da conta: '))
                a.nomeCliente = input('Nome do cliente: ')
                a.saldo = float(input('Saldo em conta: R$'))
                print('.........................')
                clientes.append(a)
                c += 1
            elif continuar == 2:
                break
            else:
                print('COMANDO INVÁLIDO')
    return clientes


def consultar(clientes):
    print('\n\nConsulta..........................')
    nomeConsulta = input('\nNome do cliente: ')
    semResultado = 0
    for i in range (len(clientes)):
        if nomeConsulta == clientes[i].nomeCliente:
            print('\nNúmero da conta: {0}\nNome do cliente: {1}\nSaldo em conta: R${2:.2f}'.format(clientes[i].numConta, clientes[i].nomeCliente, clientes[i].saldo))
            print('.........................')
        else:
            semResultado += 1
    if semResultado == len(clientes):
        print('Nenhum resultado obtido')


def excluir(clientes):
    menorSaldo = clientes[0].saldo
    for i in range (len(clientes)):
        if clientes[i].saldo < menorSaldo:
            menorSaldo = clientes[i].saldo
    for i in range (len(clientes)):
        if clientes[i].saldo == menorSaldo:
            print('\n\nO menor saldo é: ')
            print('.........................')
            print('Número da conta: {0}\nNome do cliente: {1}\nSaldo em conta: R${2:.2f}'.format(clientes[i].numConta, clientes[i].nomeCliente, clientes[i].saldo))
            print('.........................')
            print('CONTA EXCLUIDA COM SUCESSO')
            del(clientes[i])
            print('\nA lista de contas atualizada é a seguinte: ')
            for i in range (len(clientes)):
                print('\nNúmero da conta: {0}\nNome do cliente: {1}\nSaldo em conta: R${2:.2f}'.format(clientes[i].numConta, clientes[i].nomeCliente, clientes[i].saldo))
                print('.........................')


main()
