class TipoAluno: # referente ao exercício 4
    matricula = 0
    nome = ''
 
def Cadastrar(vetAluno):
    print('Cadastro de alunos.........................')
    for i in range(3):
        a = TipoAluno()
        a.matricula = int(input('Digite a matrícula: '))
        a.nome = input('Digite o nome: ')
        vetAluno.append(a)
    return vetAluno

 

def Consultar(vetAluno):
    print('Consulta por nome..........................')
    nomePesquisa = input('Qual nome quer pesquisar? ')
    for i in range(3):
        if nomePesquisa == vetAluno[i].nome:
            print('Matrícula: ',vetAluno[i].matricula,'\tNome: ',vetAluno[i].nome)
 
def Mostrar(vetAluno):
    print('Apresentaçao dos dados dos alunos..........')
    for i in range(3):
        print('Matrícula: ',vetAluno[i].matricula,'\tNome: ',vetAluno[i].nome)
 
def main():
    op = 1
    while op >=1 and op <= 3:
        print('Menu de Gerenciamento')
        print('1- Cadastrar')
        print('2- Consultar')
        print('3- Mostrar')
        print('4- Sair')
        op = int(input('Digite a opção: '))
        if op == 1:
            vetA=[]
            vetA = Cadastrar(vetA)
        elif op == 2:
            Consultar(vetA)            
        elif op == 3:
            Mostrar(vetA)
 
main()
