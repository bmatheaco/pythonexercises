


'''
Demonstração MATRIZ / LISTA para aplica-lo aos exercicios

listas

x = [1,2,3]
y = [3,2,1]
q = ['a','b','c']

w = [x,y,z]
'''

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input('Digite o valor de ['+ str(i) + ',' + str(j) + ']:')))
    matriz.append(linha)
  
#contar pares
pares = 0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            pares = pares + 1
  
#imprimir em formato de matriz
for i in range(3):
    print(matriz[i])
  
#imprimir qtde de números pares
print('A matriz contém', pares, 'números pares')
