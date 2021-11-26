class Funcionario:
    codigo = 0
    nome = ''
    salario = 0.0


def Alterar(vetFuncionario):
    print('~~Alterar Dados do Funcionario~~')
    buscarFuncionario = int(input('Digite um código para alterar seus dados: '))
    vdd = 0
    for i in range(len(vetFuncionario)):
        if vetFuncionario[i].codigo == buscarFuncionario:
            vdd = 1
            index = i
            print('Codigo do funcionario: {} \tNome: {} \tSalário: R$ {:.2f}'.format(vetFuncionario[i].codigo,
                                                                                    vetFuncionario[i].nome,
                                                                                    vetFuncionario[i].salario))
            break

    if vdd == 0:
        print('Esta pessoa não possui uma conta ou está digitado errado.')

    else:
        vetFuncionario[index].nome = str(input('Digite o nome do funcionário: '))
        vetFuncionario[index].salario = float(input('Digite o salário do funcionário: '))
        print('Codigo do funcionario: {} \tNome: {} \tSalário: R$ {:.2f}'.format(vetFuncionario[index].codigo, 
                                                                                vetFuncionario[index].nome, 
                                                                                vetFuncionario[index].salario))

    return vetFuncionario


def Excluir(vetFuncionario):
    print('~~Excluir Funcionario~~')
    buscarFuncionario = int(input('Insira o Codigo do funcionario que deseja excluir: '))
    for i in range(len(vetFuncionario)):
        if vetFuncionario[i].codigo == buscarFuncionario:
            del vetFuncionario[i]
            break
    
    Visualizar(vetFuncionario)
    return vetFuncionario


def Visualizar(vetFuncionario):
    print('~~Visualizar funcionários~~')
    for funcionario in vetFuncionario:
        print('Codigo do funcionario: {} \tNome: {} \tSalário: R$ {:.2f}'.format(funcionario.codigo,
                                                                                funcionario.nome,
                                                                                funcionario.salario))


def Cadastrar(vetFuncionario):
    print('~~Cadastro de funcionários~~')
    while 1:
        a = Funcionario()
        a.codigo = int(input('Digite o código do funcionário (Digite \'0\' para sair): '))
        if a.codigo == 0:
            break
        a.nome = str(input('Digite o nome do funcionário: '))
        a.salario = float(input('Digite o salário do funcionário: '))
        vetFuncionario.append(a)
        print('Codigo do funcionario: {} \tNome: {} \tSalário: R$ {:.2f}'.format(a.codigo, a.nome, a.salario))
    return vetFuncionario


def Main():
    vetTipoFuncionario=[]
    op = 1
    while op >=1 and op <= 4:
        print('~~Menu de Gerenciamento~~')
        print('1- Cadastrar')
        print('2- Visualizar')
        print('3- Excluir')
        print('4- Alterar')
        print('5- Sair')
        op = int(input('Digite a opção: '))
        if op == 1:
            vetTipoFuncionario = Cadastrar(vetTipoFuncionario)
        elif op == 2:
            Visualizar(vetTipoFuncionario)
        elif op == 3:
            vetTipoFuncionario = Excluir(vetTipoFuncionario)
        elif op == 4:
            vetTipoFuncionario = Alterar(vetTipoFuncionario)

Main()