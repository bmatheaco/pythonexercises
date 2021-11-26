matriz = []
for i in range(2):
    linha = []
    for j in range(3): # coluna = 3 serviços prestados no dia
        ''' aqui será algo parecido com o tipo aluno
        a = TipoAluno()
        a.matricula = int(input('Digite a matrícula: '))
        a.nome = input('Digite o nome: ')
        '''
        linha.append(int(input('Digite o valor de ['+ str(i) + ',' + str(j) + ']:')))
    matriz.append(linha)
 
#contar pares
pares = 0
for i in range(3): # linha
    for j in range(3): # coluna
        if matriz[i][j].valor % 2 == 0:
            pares = pares + 1
 
#imprimir em formato de matriz
for i in range(3):
    print(matriz[i])
 
#imprimir qtde de números pares
print('A matriz contém', pares, 'números pares')
