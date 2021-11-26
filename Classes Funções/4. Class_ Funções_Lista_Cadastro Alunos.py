
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



class TipoAluno:
  nome = ' '
  matricula = 0
  data_N = ''
  telefone = 0
  endereco = ''
  numero = 0
  bairro = ''
  cidade = ''
  serie = 0



def cadastrar(vetAluno):
    print('------- CADASTRO DOS ALUNOS -------')
    for i in range(2):
        a = TipoAluno()
        a.matricula = int(input('Matrícula Nº: '))
        a.nome = input('Nome Completo do Aluno: ')
        a.data_N = input('Data de Nascimento (Ex: 00/00/0000): ')
        a.telefone = int(input('Número de Telefone: '))
        a.endereco = input('ENDEREÇO: Rua / AV - ')
        a.numero = int(input('Número: '))
        a.bairro = input('Bairro: ')
        a.cidade = input('Cidade: ')
        a.serie = input('Série do Aluno: ')
        print()
        vetAluno.append(a)
    return vetAluno


        
      
def consultar(vetAluno):
    print('------- CONSULTA ALUNOS MATRICULADOS -------')
    nomePesquisa = input('Informe Nome do Aluno: ')
    print()
    for i in range(2):
        if nomePesquisa == vetAluno[i].nome:
            print('********** RESULTADO ENCONTRADO ********')
            print('.......')
            print('Matricula: ', vetAluno[i].matricula)
            print('Nome: ', vetAluno[i].nome)
            print('Data de Nascimento: ', vetAluno[i].data_N)
            print('Telefone: ', vetAluno[i].telefone)
            print('',vetAluno[i].serie,'º série')

        
          
def mostrar(vetAluno):
    print('------- REGISTRO DE DADOS ALUNOS -------')
    print()
    for i in range(2):
        print('__________________________________')
        print('Matricula: ', vetAluno[i].matricula)
        print('Nome: ', vetAluno[i].nome)
        print('Data de Nascimento: ', vetAluno[i].data_N)
        print('Telefone: ', vetAluno[i].telefone)
        print('Endereço: ', vetAluno[i].endereco)
        print('Numero: ', vetAluno[i].numero)
        print('Bairro: ', vetAluno[i].bairro)
        print('Cidade: ', vetAluno[i].cidade)
        print('',vetAluno[i].serie,'º série')
       
 
def main():
    op = 1
    while op >=1 and op <= 3:
        print('------ MENU DE GERENCIAMENTO --------')
        print('1- Cadastrar')
        print('2- Consultar')
        print('3- Mostrar')
        print('4- Sair')
        op = int(input('Digite a opção: '))
        print()
        if op == 1:
            vetA=[]
            vetA = cadastrar(vetA)
        elif op == 2:
            consultar(vetA)            
        elif op == 3:
            mostrar(vetA)
        elif op == 4:
          print('Sair!')
          break
         
main()




