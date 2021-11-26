"""
7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:
*** Minha Calculadora ***
Digite um número.....:
Digite outro número..:
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja?
b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos,
quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.
"""


def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}\n{"~"* 50}')


def subtracao(a, b):
    sub = a - b
    print(f'{a} - {b} = {sub}\n{"~"* 50}')


def multiplicacao(a, b):
    mul = a * b
    print(f'{a} x {b} = {mul:.1f}\n{"~"* 50}')


def divisao(a, b):
    div = a / b
    print(f'{a} / {b} = {div:.1f}\n{"~"*50}')


while True:
    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira outro número: '))
    opc = str(input(f'''{' Calculadora ':=^50}
[ + ] - Soma
[ - ] - Subtração
[ x ] - Multiplicação
[ / ] - Divisão
[ S ] - Sair
{"=" * 50} 
Opção: '''))
    if opc in 'Ss':
        print('Fechando calculadora')
        break
    if opc not in ('+', '-', 'x', '/'):
        print('[ ERRO ] OPÇÃO INVÁLIDA! Tente novamente')
    print(F'{" RESULTADO ":~^50}')
    if opc == '+':
        soma(num1, num2)
    elif opc == '-':
        subtracao(num1, num2)
    elif opc == 'x':
        multiplicacao(num1, num2)
    elif opc == '/':
        divisao(num1, num2)
