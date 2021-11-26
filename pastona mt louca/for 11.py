gordo = 0
magro = 1000
peso = []
nome = []
for i in range(4):
  peso.append(float(input('Informe um peso: ')))
  nome.append(input('Informe um nome: '))
  if peso[i] > gordo:
    gordo = peso[i]
    nomeg = nome[i]
  if peso[i] < magro:
    magro= peso[i]
    nomem= nome[i]
print('Peso do gordo ',gordo,'Nome: ',nomeg)
print('Peso do magro ',magro,'Nome: ',nomem)
