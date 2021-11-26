class aluno:
  matricula = 0
  nome = ' '
  data_de_nascimento = ' '
  serie = ' '
  telefone = 0
  endereco = ' '


def Mostrar(vetAluno):
    print('~~Apresentação dos dados dos alunos~~')
    for aluno in vetAluno:
        print('Matrícula: ',aluno.matricula,'\tNome: ',aluno.nome,'\tData de nascimento: ',aluno.data_de_nascimento,
                '\tSerie: ',aluno.serie,'\tTelefone: ',aluno.telefone,'\tEndereço:',aluno.endereco)


def Consultar(vetAluno):
    print('~~Consulta por nome~~')
    nomePesquisa = input('Qual nome quer pesquisar? ')
    for aluno in vetAluno:
        if nomePesquisa == aluno.nome:
            print('Matrícula: ',aluno.matricula,'\tNome: ',aluno.nome,'\tData de nascimento: ',aluno.data_de_nascimento,
                  '\tSerie: ',aluno.serie,'\tTelefone: ',aluno.telefone,'\tEndereço:',aluno.endereco)


def Cadastrar(vetAluno):
  c = 1
  while c > 0 and c <= 500:
    a = aluno()
    print('~~Cadastro de alunos~~')
    a.matricula = int(input('Digite a Matrícula (Digite \'0\' para sair): '))
    if a.matricula == 0:
      break
    a.nome = str(input('Digite o nome: '))
    a.data_de_nascimento = str(input('Digite a data de nascimento: '))
    a.serie =str(input('Digite a serie: '))
    a.telefone = int(input('Digite o telefone: '))
    a.endereco = str(input('Digite o endereço: '))
    c += 1
    vetAluno.append(a)
    print('Matrícula: ',a.matricula,'\tNome: ',a.nome,'\tData de nascimento: ',a.data_de_nascimento,
            '\tSerie: ',a.serie,'\tTelefone: ',a.telefone,'\tEndereço:',a.endereco)
  return vetAluno


def main():
    op = 1
    while op >=1 and op <= 3:
        print('~~Menu de Gerenciamento~~')
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
