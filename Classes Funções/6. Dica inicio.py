'''
6.
    
'''

# EXPLICAÇÃO DA PARTE INICIAL DO EXERCÍCIO 6
 
classTipoServico: # referente ao exercício 6
    codigo = 0#código do serviço
    descricao = ''# descrição do serviço
 
classTipoServicoPrestado:
    numeroServico = 0
    codigoServico = 0
    precoServico = 0.0
    codigoCliente = 0
 
'''se quiserem, mas não é necessário
class TipoCliente:
    codigo = 0
    nome = ''          '''
 
defCadastrarTiposServico(vTipoServico):
print('Cadastro dos tipos de serviços.........................')
for i inrange(4):
        ts = TipoServicoPrestado()
        ts.codigo = int(input('Digite o código do serviço prestado: '))
        ts.descricao = input('Digite a descrição do serviço: ')
        vTipoServico.append(ts)
return vTipoServico
 
defMostrarTipoServico(vTipoServico):
[11:31] GIOVANA ANGELICA ROS MIOLA
    

# EXPLICAÇÃO DA PARTE INICIAL DO EXERCÍCIO 6
 
classTipoServico: # referente ao exercício 6
    codigo = 0#código do serviço
    descricao = ''# descrição do serviço
 
classTipoServicoPrestado:
    numeroServico = 0
    codigoServico = 0
    precoServico = 0.0
    codigoCliente = 0
 
'''se quiserem, mas não é necessário
class TipoCliente:
    codigo = 0
    nome = ''          '''
 
defCadastrarTiposServico(vTipoServico):
print('Cadastro dos tipos de serviços.........................')
for i inrange(4):
        ts = TipoServicoPrestado()
        ts.codigo = int(input('Digite o código do serviço prestado: '))
        ts.descricao = input('Digite a descrição do serviço: ')
        vTipoServico.append(ts)
return vTipoServico
 
defMostrarTipoServico(vTipoServico):
print('Apresentaçao dos tipos de serviço prestados..........')
for i inrange(len(vTipoServico)):
print('Código: ',vTipoServico[i].codigo,'\tDescrição: ',vTipoServico[i].descricao)
 
defmain():
    op = 1
while op >=1and op <= 2:
print('Menu de Gerenciamento')
print('1- Cadastrar tipo de serviço')
print('2- Mostrar tipos de serviço')
print('3- Cadastrar a prestação de serviço') # MATRIZ DE 30 LINHAS E 3 COLUNAS
print('4- Mostrar todas as prestações de serviço')
print('5- Sair')
        op = int(input('Digite a opção: '))
if op == 1:
            vetTipoServico=[]
            vetTipoServico = CadastrarTiposServico(vetTipoServico)          
elif op == 2:
            MostrarTipoServico(vetTipoServico)

main()

print('Código: ',vTipoServico[i].codigo,'\tDescrição: ',vTipoServico[i].descricao)
 
defmain():
    op = 1
while op >=1and op <= 2:
print('Menu de Gerenciamento')
print('1- Cadastrar tipo de serviço')
print('2- Mostrar tipos de serviço')
print('3- Cadastrar a prestação de serviço') # MATRIZ DE 30 LINHAS E 3 COLUNAS
print('4- Mostrar todas as prestações de serviço')
print('5- Sair')
        op = int(input('Digite a opção: '))
if op == 1:
            vetTipoServico=[]
            vetTipoServico = CadastrarTiposServico(vetTipoServico)          
elif op == 2:
            MostrarTipoServico(vetTipoServico)

main()

<https://teams.microsoft.com/l/message/19:9207998693024519a3a77c9561111d2f@thread.tacv2/1592663499011?tenantId=cf72e2bd-7a2b-4783-bdeb-39d57b07f76f&amp;groupId=d762d60c-ffef-4cae-b7a7-e10c5511f7ff&amp;parentMessageId=1592662357724&amp;teamName=Linguagem de Programacao-A-N-ADS-PPR-20201&amp;channelName=Geral&amp;createdTime=1592663499011>
