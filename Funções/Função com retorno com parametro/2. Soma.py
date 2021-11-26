'''
2. (Função com retorno com parâmetro) Faça um programa contendo uma
função/método que receba dois números via parâmetro, some os dois valores,
retorne e apresente o resultado.

'''

def soma(a,b):
    c = a + b
    return c

x = int(input('Adicione um número:  '))
y = int(input('Adicione um número:  '))
s = soma(x,y)
print('O resultado é da soma é: ',s)



'''
RESULTADO:

Adicione um número:  15
Adicione um número:  15
O resultado é da soma é:  30

'''
