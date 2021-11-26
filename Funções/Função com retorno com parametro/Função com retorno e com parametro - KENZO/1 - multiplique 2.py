"""
 1. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba por parâmetro 
 um número e o multiplique por 2, retorne e apresente o resultado da função.
"""
def mult2(valor):
    mult = valor * 2
    return mult

num = int(input('Insira um número para ser multiplicado por 2: '))
print(f'{num} x 2 = {mult2(num)}')
