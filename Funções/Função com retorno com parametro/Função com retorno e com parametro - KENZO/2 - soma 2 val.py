"""
2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números
via parâmetro, some os dois valores, retorne e apresente o resultado.
"""
def soma(a, b):
    s = a + b
    return s

num1 = int(input('Valor 1: '))
num2 = int(input('Valor 2: '))
print(f'{num1} + {num2} = {soma(num1, num2)}')