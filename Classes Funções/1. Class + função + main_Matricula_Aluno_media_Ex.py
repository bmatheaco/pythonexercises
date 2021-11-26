class tipoAluno: 
    matricula = 0
    nome = ''
    p1 = 0.0
    p2 = 0.0
    media = 0.0


def main(): #Principal
    a = tipoAluno() #Contrutor da classe
    a.matricula = int(input('Digite nº da matricula'))
    a.nome = input('Informe o nome do aluno')
    a.p1 = float(input('Informe nota P1: '))
    a.p2 = float(input('Informe nota P2: '))
    a.media = (a.p1 + a.p2)/2
    print('Media = ',a.media)

   
main()

#EXEMPLO - Para o uso de lista
'''
lista = []
for i in range(1,6:)
    a = tipoAluno() #Contrutor da classe
    a.matricula = int(input('Digite nº da matricula'))
    a.nome = input('Informe o nome do aluno')
    a.p1 = float(input('Informe nota P1: '))
    a.p2 = float(input('Informe nota P2: '))
    a.media = (a.p1 + a.p2)/2
    print('Media = ',a.media)

    lista.append(a)
        print('1[0]...', a[i].nome)#indice da lista




 Código: {produtos[0].codigo}. \
        Nome: {produtos[0].nome}. \
        Preço: R$ {produtos[0].preco:.2f}.')
'''


