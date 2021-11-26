'''
7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:
a) Função para construir um menu de opções para uma calculadora:

Exemplo:

*** Minha Calculadora ***
Digite um número.....: 
Digite outro número..: 
    + Soma dois números
    - Subtrai dois números
    * Multiplica dois números
    / Divide dois números
Qual opção deseja? 
--------------------------------------

b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

Observação:

Na chamada da função deve-se utilizar uma estrutura de repetição que permita
diversos cálculos, quando o usuário quiser sair da calculadora digitará
qualquer valor diferente dos caracteres do menu.

A função de desenho/construção do menu, chamará todas as outras passando a
elas os valores digitados.

'''

def soma():
    x = float(input("Primeiro Número: "))
    y = float(input("Segundo Número: "))
    print()
    print("A Soma é: ",x+y)
    print()

    

def subtracao():
    x = float(input("Primeiro Número: "))
    y = float(input("Segundo Número: "))
    print()
    print("O Resultado da Subtração é: ",x-y)
    print()
    
    

def multiplicacao():
    x = float(input("Primeiro Número: "))
    y = float(input("Segundo Número: "))
    print()
    print("O Resultado da Multiplicação é: ",x*y)
    print()
    
    

def divisao():
    x = float(input("Primeiro Número: "))
    y = float(input("Segundo Número: "))
    print()
    print("O Resultado da Divisão é: ",x/y)
    print()
    

opcao=1

while opcao:
    print ("----------------------------------")

    print ("**** CALCULADORA ****")
    print()
    print("MENU")
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    print()

    opcao = int(input("Opção Escolhida: "))
    
    
    print ()

    if opcao==1:
        soma()
    if opcao==2:
        subtracao()
    if opcao==3:
        multiplicacao()
    if opcao==4:
        divisao()
  


'''

RESULTADO:

----------------------------------
**** CALCULADORA ****

MENU
0. Sair
1. Somar
2. Subtrair
3. Multiplicação
4. Divisão 

Opção Escolhida: 1

Primeiro Número: 65
Segundo Número: 70

A Soma é:  135.0

----------------------------------
**** CALCULADORA ****

MENU
0. Sair
1. Somar
2. Subtrair
3. Multiplicação
4. Divisão 

Opção Escolhida: 2

Primeiro Número: 36
Segundo Número: 25

O Resultado da Subtração é:  11.0

----------------------------------
**** CALCULADORA ****

MENU
0. Sair
1. Somar
2. Subtrair
3. Multiplicação
4. Divisão 

Opção Escolhida: 0


'''
