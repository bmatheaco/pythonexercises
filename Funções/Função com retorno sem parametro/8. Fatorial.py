'''
8. (Função com retorno sem parâmetro) Faça uma função/método que leia e
armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B,
de mesmo tamanho, que armazenará o fatorial de cada elemento de A.
Retorne/apresente o vetor B.

'''

def armazenamento():
  a = []
  b = []
  for x in range(5):
    a.append(int(input( "Informe um Valor: " )))
    f = 1
    for y in range(a[x],1,-1):
      f *= y
    b.append(f)
  return b

print(armazenamento())

'''
# RESULTADO....

Informe um Valor: 2
Informe um Valor: 4
Informe um Valor: 6
Informe um Valor: 3
Informe um Valor: 1
[2, 24, 720, 6, 1]

'''
