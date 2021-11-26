'''
6. Uma empresa prestadora de serviços armazena informações sobre os serviços prestados. Sabe-se que a empresa pode realizar no máximo três serviços diariamente. É de interesse de sua direção manter um histórico mensal (30 dias) sobre os serviços prestados.
A empresa realiza quatro tipos de serviços:

1) pintura;
2) jardinagem;
3) faxina e
4) reforma em geral.

Cada serviço realizado deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente.
Cadastre os quatro tipos de serviços (código e descrição) que a empresa poderá realizar. Para isso, utilize um vetor de quatro posições. O programa deverá mostrar o seguinte menu de opções:
Cadastrar os tipos de serviços
Cadastrar os serviços prestados
Mostrar os serviços prestados em determinado dia
Mostrar os serviços prestados dentro de um intervalo de valor
Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
Para a opção 1: deve-se cadastrar os tipos de serviços oferecidos pela empresa, com código e descrição.

Para a opção 2: deve-se considerar que deverão ser cadastrados os serviços prestados ao logo do mês. Em cada dia podem ser cadastrados, no máximo, três serviços prestados.

Utilize uma matriz capaz de armazenar em cada posição todas as informações referentes a um serviço prestado (número, valor, código do serviço,código do cliente). Cada linha representa um dia do mês. Dessa maneira, considere a matriz com dimensão 30 × 3.
Solicite o dia em que o serviço foi prestado e as demais informações. Lembre-se de que a empresa só pode prestar os serviços que já tenham sido cadastrados no vetor de tipo de serviços.

Caso o usuário digite um código de tipo de serviço inválido, o programa deverá mostrar uma mensagem de erro.

Quando o usuário tentar cadastrar mais de três serviços prestados em um mesmo dia, também deverá mostrar uma mensagem de erro.

Para a opção 3: o programa deverá receber o dia que se deseja consultar e mostrar os respectivos serviços prestados.

Para a opção 4: o programa deverá receber o valor mínimo e o valor máximo e mostrar os serviços prestados que estiverem nesse intervalo.

Para a opção 5: o programa deverá mostrar todos os serviços prestados, conforme o exemplo a seguir.

'''
class Tipo_Serv:
    codigo = 0
    descricao = ''


class Serv_Prest:
    num_Serv = 0
    cod_Serv = 0
    preco_Serv = 0.0
    cod_Cliente = 0


def Relatorio_Dia(vet_Serv_Prest, vet_Tipo_Serv):#5
    print('=== Apresentaçao Serviço Prestados ===')
    print(vet_Tipo_Serv)
    for i in range(len(vet_Serv_Prest)):
        if len(vet_Serv_Prest[i]) > 0:
            print('\nDia {}:\n'.format(i+1))
            for j in range(len(vet_Serv_Prest[i])):
                for k in range(len(vet_Tipo_Serv)):
                    if vet_Serv_Prest[i][j].cod_Serv == vet_Tipo_Serv[k].codigo:
                        d = vet_Tipo_Serv[k].descricao
                print('|||Número serviço: ',vet_Serv_Prest[i][j].num_Serv,
                    '||| Código Serviço: ',vet_Serv_Prest[i][j].cod_Serv,
                    '\n||| Descrição serviço: ',d,
                    '||| Preço do serviço: R$ {:.2f}'.format(vet_Serv_Prest[i][j].preco_Serv),
                    '||| Código  Cliente: ',vet_Serv_Prest[i][j].cod_Cliente)
    print('')


def mostrar_Serv_Valor(vet_Serv_Prest):#4
    print('--- Apresentaçao de serviços entre o intervalo de dois ---')
    minimo = float(input('== Valor Minimo que deseja procurar: '))
    maximo = float(input('== Valor Maximo que deseja procurar: '))
    for i in range(len(vet_Serv_Prest)):
        if len(vet_Serv_Prest[i]) > 0:
            for j in range(len(vet_Serv_Prest[i])):
                if vet_Serv_Prest[i][j].preco_Serv >= minimo and vet_Serv_Prest[i][j].preco_Serv <= maximo:
                    print('\nDia {}:\n'.format(i+1))
                    print('||| Número do serviço: ',vet_Serv_Prest[i][j].num_Serv,
                        '||| Código do Serviço: ',vet_Serv_Prest[i][j].cod_Serv,
                        '\n||| Preço do serviço: R$ {:.2f}'.format(vet_Serv_Prest[i][j].preco_Serv),
                        '||| Código do Cliente: ',vet_Serv_Prest[i][j].cod_Cliente)
    print('')


def mostrar_Serv_Dia(vet_Serv_Prest):#3
    print('===== Pesquisa de serviço prestados por dia =====')
    dia = int(input('- Insira o dia que deseja visualizar os serviços: '))
    if len(vet_Serv_Prest[dia-1]) > 0:
        print('\nDia {}:\n'.format(dia))
        for j in range(len(vet_Serv_Prest[dia-1])):
            print('|| Número do serviço: ',vet_Serv_Prest[dia-1][j].num_Serv,
                '|| Código do Serviço: ',vet_Serv_Prest[dia-1][j].cod_Serv,
                '\n|| Preço do serviço: R$ {:.2f}'.format(vet_Serv_Prest[dia-1][j].preco_Serv),
                '||| Código do Cliente: ',vet_Serv_Prest[dia-1][j].cod_Cliente)
            print()
    else:
        print('\nNeste dia não existe nenhum registro de serviços a serem prestados.')
    print('')


def cadastrar_Prest_Serv (vet_Serv_Prest, vet_Tipo_Serv):#2
    print('--- Cadastro Prestação de Serviço ---')
    while 1:
        dia = int(input('\nInforme o dia que deseja cadastrar o serviço - 0 para sair: '))
        if dia == 0:
            break
        if 3-len(vet_Serv_Prest[dia-1]) == 0:
            print('\nNão é possivel reservar mais serviços nesse dia.')
        else:
            print('\n{}º dia do mês de serviço prestado: '.format(dia))
            dias = vet_Serv_Prest[dia-1]
            for j in range(3-len(vet_Serv_Prest[dia-1])):
                print('\n     {}º serviço prestado do dia: '.format(len(vet_Serv_Prest[dia-1])+1))
                b = Serv_Prest()
                b.num_Serv = int(input('- Informe Nº. Serviço - 0 para Sair: '))
                if b.num_Serv == 0:
                    break
                while 1:
                    b.cod_Serv = int(input('- Digite o código do serviço: '))
                    existe = False
                    for k in range(len(vet_Tipo_Serv)):
                        if vet_Tipo_Serv[k].codigo == b.cod_Serv:
                            existe = True
                            break
                    if existe:
                        break
                    else:
                        print('Não existe esse tipo de serviço!!')
                b.preco_Serv = float(input('- Digite o preço do serviço: R$ '))
                b.cod_Cliente = int(input('- Digite o código do cliente: '))
                dias.append(b)
            vet_Serv_Prest[dia-1] = dias
    print('')
    return vet_Serv_Prest



def mostrar_Tipo_Serv(vet_Tipo_Serv):
    print('--- Apresentaçao Tipos de Serviços Prestados ----\n')
    for i in range(len(vet_Tipo_Serv)):
        print('||| Código: ',vet_Tipo_Serv[i].codigo,' ||| Descrição: ',vet_Tipo_Serv[i].descricao)



def cadastrar_Tipos_Serv (vet_Tipo_Serv):#1
    print('--- Cadastro Tipos de Serviços ---')
    print('--- Serviços já cadastrados: ---')
    mostrar_Tipo_Serv(vet_Tipo_Serv)
    while 1:
        a = Tipo_Serv()
        a.codigo = int(input('CÓDIGO SERVIÇO PRESTADO - 0 para sair): '))
        if a.codigo == 0:
            break
        a.descricao = str(input('- Descrição do serviço: \n'))
        vet_Tipo_Serv.append(a)
    return vet_Tipo_Serv


def iniciar_Mat(vetor):
    for i in range(30):
        vetor.append([])
    return vetor


def main():
    vet_Tipo_Serv=[]
    vet_Serv_Prest=[]
    vet_Serv_Prest = iniciar_Mat(vet_Serv_Prest)
    op = 1
    while op >=1 and op <= 5:
        print('\n-------- Menu de Gerenciamento --------')
        print('1 - Cadastrar Tipo de Serviço')
        print('2 - Cadastrar Serviços Prestados') 
        print('3 - Mostrar os Serviços Prestados: Pesquisa por Dia')
        print('4 - Mostrar os Serviços Prestados: Pesquisa por Valor')
        print('5 - Mostrar Relatório Geral por dia e descrição do tipo do serviço')
        print('6 - Sair')
        op = int(input('Digite a opção: '))
        print()
        if op == 1:
            vet_Tipo_Serv = cadastrar_Tipos_Serv(vet_Tipo_Serv)          
        elif op == 2:
             vet_Serv_Prest = cadastrar_Prest_Serv(vet_Serv_Prest, vet_Tipo_Serv) 
        elif op == 3:
            mostrar_Serv_Dia(vet_Serv_Prest)
        elif op == 4:
            mostrar_Serv_Valor(vet_Serv_Prest)          
        elif op == 5:
            Relatorio_Dia(vet_Serv_Prest, vet_Tipo_Serv)
 
main()
