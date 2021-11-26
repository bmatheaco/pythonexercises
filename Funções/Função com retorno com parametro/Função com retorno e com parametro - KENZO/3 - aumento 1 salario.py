"""
3. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem
de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.
"""
def aumento(valor):
    novo_salario = salario + salario*(valor / 100)
    return novo_salario

salario = float(input('Salário do funcionário'))
porcentagem = int(input('Porcentagem do aumento: '))
print(f'O salário de R${salario}, com {porcentagem}% de aumento, foi para: R${aumento(porcentagem)}')