class TipoServico:
    codigo = 0
    descricao = ''


class TipoServicoPrestado:
    num_Serv = 0
    cod_Serv = 0
    preco_Serv = 0.0
    cod_Cliente = 0


def mostrarRelatorioPorDia(vServicoPrestado, vTipoServico):#5
    print('~Apresentaçao de serviço prestados~')
    print(vTipoServico)
    for i in range(len(vServicoPrestado)):
        if len(vServicoPrestado[i]) > 0:
            print('\nDia {}:\n'.format(i+1))
            for j in range(len(vServicoPrestado[i])):
                for k in range(len(vTipoServico)):
                    if vServicoPrestado[i][j].codigoServico == vTipoServico[k].codigo:
                        des = vTipoServico[k].descricao
                print('Número do serviço: ',vServicoPrestado[i][j].numeroServico,
                    '| Código do Serviço: ',vServicoPrestado[i][j].codigoServico,
                    '| Descrição do serviço: ',des,
                    '| Preço do serviço: R$ {:.2f}'.format(vServicoPrestado[i][j].precoServico),
                    '| Código do Cliente: ',vServicoPrestado[i][j].codigoCliente)
    print('')


def mostrarServicosEmValor(vServicoPrestado):#4
    print('~Apresentaçao de serviços entre o intervalo de dois~')
    minimo = float(input('Insira o valor minimo que deseja procurar: '))
    maximo = float(input('Insira o valor maximo que deseja procurar: '))
    for i in range(len(vServicoPrestado)):
        if len(vServicoPrestado[i]) > 0:
            for j in range(len(vServicoPrestado[i])):
                if vServicoPrestado[i][j].precoServico >= minimo and vServicoPrestado[i][j].precoServico <= maximo:
                    print('\nDia {}:\n'.format(i+1))
                    print('Número do serviço: ',vServicoPrestado[i][j].numeroServico,
                        '| Código do Serviço: ',vServicoPrestado[i][j].codigoServico,
                        '| Preço do serviço: R$ {:.2f}'.format(vServicoPrestado[i][j].precoServico),
                        '| Código do Cliente: ',vServicoPrestado[i][j].codigoCliente)
    print('')


def mostrarServicosEmDia(vServicoPrestado):#3
    print('~Pesquisa de serviço prestados por dia~')
    dia = int(input('Insira o dia que deseja visualizar os serviços: '))
    if len(vServicoPrestado[dia-1]) > 0:
        print('\nDia {}:\n'.format(dia))
        for j in range(len(vServicoPrestado[dia-1])):
            print('Número do serviço: ',vServicoPrestado[dia-1][j].numeroServico,
                '| Código do Serviço: ',vServicoPrestado[dia-1][j].codigoServico,
                '| Preço do serviço: R$ {:.2f}'.format(vServicoPrestado[dia-1][j].precoServico),
                '| Código do Cliente: ',vServicoPrestado[dia-1][j].codigoCliente)
    else:
        print('\nNeste dia nao existe nenhum registro de serviços a serem prestados.')
    print('')


def inicializarMatrix(vetor):
    for i in range(30):
        vetor.append([])
    return vetor


def cadastrarPrestacaoDeServico(vServicoPrestado, vTipoServico):#2
    print('~Cadastro de prestação de serviço~')
    while 1:
        dia = int(input('\nInforme o dia que deseja cadastrar o serviço(insira 0 para sair): '))
        if dia == 0:
            break
        if 3-len(vServicoPrestado[dia-1]) == 0:
            print('\nNão é possivel reservar mais serviços nesse dia.')
        else:
            print('\n{}º dia do mes de serviço prestado: '.format(dia))
            dias = vServicoPrestado[dia-1]
            for j in range(3-len(vServicoPrestado[dia-1])):
                print('\n     {}º serviço prestado do dia: '.format(len(vServicoPrestado[dia-1])+1))
                tsp = TipoServicoPrestado()
                tsp.numeroServico = int(input('Digite o numero do serviço (insira 0 para sair): '))
                if tsp.numeroServico == 0:
                    break
                while 1:
                    tsp.codigoServico = int(input('Digite o código do serviço: '))
                    existe = False
                    for k in range(len(vTipoServico)):
                        if vTipoServico[k].codigo == tsp.codigoServico:
                            existe = True
                            break
                    if existe:
                        break
                    else:
                        print('Não existe esse tipo de serviço!!')
                tsp.precoServico = float(input('Digite o preço do serviço: R$ '))
                tsp.codigoCliente = int(input('Digite o código do cliente: '))
                dias.append(tsp)
            vServicoPrestado[dia-1] = dias
    print('')
    return vServicoPrestado


def mostrarTipoServico(vTipoServico):
    print('~Apresentaçao dos tipos de serviços prestados~')
    for i in range(len(vTipoServico)):
        print('Código: ',vTipoServico[i].codigo,' | Descrição: ',vTipoServico[i].descricao)


def cadastrarTiposServico(vTipoServico):#1
    print('~Cadastro dos tipos de serviços~')
    print('Serviços ja cadastrados:')
    mostrarTipoServico(vTipoServico)
    while 1:
        ts = TipoServico()
        ts.codigo = int(input('Digite o código do serviço prestado (insira 0 para sair): '))
        if ts.codigo == 0:
            break
        ts.descricao = str(input('Digite a descrição do serviço: '))
        vTipoServico.append(ts)
    return vTipoServico


def main():
    vetTipoServico=[]
    vetServicoPrestado=[]
    vetServicoPrestado = inicializarMatrix(vetServicoPrestado)
    op = 1
    while op >=1 and op <= 5:
        print('~Menu de Gerenciamento~')
        print('1- Cadastrar tipo de serviço')
        print('2- Cadastrar a serviços prestados') # MATRIZ DE 30 LINHAS E 3 COLUNAS
        print('3- Mostrar os serviços prestados em determinado dia')
        print('4- Mostrar os serviços prestados dentro de um intervalo de valor')
        print('5- Mostrar relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço')
        print('6- Sair')
        op = int(input('Digite a opção: '))
        if op == 1:
            vetTipoServico = cadastrarTiposServico(vetTipoServico)          
        elif op == 2:
            vetServicoPrestado = cadastrarPrestacaoDeServico(vetServicoPrestado, vetTipoServico)
        elif op == 3:
            mostrarServicosEmDia(vetServicoPrestado)
        elif op == 4:
            mostrarServicosEmValor(vetServicoPrestado)
        elif op == 5:
            mostrarRelatorioPorDia(vetServicoPrestado, vetTipoServico)
 
main()
