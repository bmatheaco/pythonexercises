soma = 0
print('Insira 4 numeros diferentes abaixo:')
for a in range(1,5):
    n= float(input('Insira o {}º numero: '.format(a)))
    soma += n
print('A soma dos 4 valores foi: ',soma)
