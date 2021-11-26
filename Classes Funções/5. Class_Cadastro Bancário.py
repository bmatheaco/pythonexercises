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
##### Á FINALIZAR #####

class info:
   n_conta = 0
   nome = ' '
   saldo = 0.0


def excluir(vet_I):
    print('\n EXCLUIR CONTA ')
    print('---------------------\n')

    menor_V = 0
    for i in range (len(vet_I.saldo)):
       menor_V == min(vet_I.saldo)
       print(menor_v)
   





'''    
    
       if i == 0:
          menorSaldo = vet_I[i].saldo
          conta = i
       else:
          if vet_I[i].saldo < menorSaldo:
             menorSaldo = saldo
             conta = i
             
       vet_I.pop(conta)



        if vet_I[i].saldo < menorSaldo:
            menorSaldo = vet_I[i].saldo
    for i in range (len(vet_I)):
        if vet[i].saldo == menorSaldo:
            print('\n\nO menor saldo é: ')
            print('.........................')
            print('Número da conta: {0}\nNome do cliente: {1}\nSaldo em conta: R${2:.2f}'.format(vet_I[i].n_conta, vet_I[i].nome,vet_I[i].saldo))
            print('.........................')
            print('CONTA EXCLUIDA COM SUCESSO')
            del(vet_I[i])
            print('\nA lista de contas atualizada é a seguinte: ')
            for i in range (len(vet_I)):
                print('\nNúmero da conta: {0}\nNome do cliente: {1}\nSaldo em conta: R${2:.2f}'.format(vet_I[i].n_conta, vet_I[i].nome,vet_I[i].saldo))
                print('.........................')

'''
    
def consultar(vet_I):
    print('\nVISUALIZAR CONTAS DUPLICADAS E/OU DO MESMO CLIENTE')
    print('-----------------------------------------------------\n')
    nomePesquisa = input('- Cliente à Consultar: ').upper()
    for i in range(len(vet_I)):
        if nomePesquisa.upper() in vet_I[i].nome.upper():
           print('********** RESULTADO ENCONTRADO ********')
           print('Conta Nº: ',vet_I[i].n_conta, '\tNome: ',vet_I[i].nome)
           print('Saldo em Conta: R$ ',vet_I[i].saldo)
        

          
def cadastro(vet_I):
   for i in range(2): 
      a = info()
      print('................................')
      print('INFORME CORRETAMENTE OS DADOS:')
      print('................................\n')

      a.n_conta = int(input('- Conta Corrente Número: '))
      a.nome = str(input('- Nome Completo: ')).upper()
      a.saldo = float(input('- Saldo Bancário R$: '))
      vet_I.append(a)
   return vet_I
   
   
def main():
    op = 1
    while op >=1 and op <= 4:
        print('\nMenu de Gerenciamento:')
        print('--------------------------')
        print('1- Cadastrar Contas')
        print('2- Consultar Cliente')
        print('3- Excluir Conta: Menor Saldo')
        print('4- Sair')
        print()

        op = int(input('Digite a opção: '))
        print()
        if op == 1:
            vet_info =[]
            vet_info = cadastro(vet_info)
        elif op == 2:
            consultar(vet_info)            
        elif op == 3:
            excluir(vet_info)
        elif op == 4:
            print('---- Sair! ----')
            break
        else:
            print('Operação Inválida')




main()

            
