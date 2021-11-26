'''
3. (Função com retorno com parâmetro) Faça um programa contendo uma
função/método que receba um valor de porcentagem de aumento via parâmetro,
aplique este aumento a um salário de um funcionário, retorne e apresente o
novo salário.

'''

def aumento(a):
    b = a * (12/ 100)
    return b

print('--- Reajuste Salarial de 12% ---')
x = int(input('Informe Salário Atual: R$ '))
p = aumento(x)
print('O Reajuste do valor é de: R$ ',p)
print()
print('R$ ',x + p,'é o valor atualizado')



'''
RESULTADO:

--- Reajuste Salarial de 12% ---
Informe Salário Atual: R$ 1500
O Reajuste do valor é de: R$  180.0

R$  1680.0 é o valor atualizado

'''
