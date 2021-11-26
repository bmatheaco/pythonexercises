'''
5. (Função com retorno com parâmetro) Faça um programa contendo uma
função/método que receba um valor de porcentagem de aumento e um salário
via parâmetro, aplique este aumento ao salário do funcionário.
Na parte principal do programa, na chamada da função, utilize um laço de
repetição para ler 10 salários, chame a função para aplicar o aumento e gerar
o novo salário, ainda dentro da estrutura de repetição acumule os novos
salários e ao final apresente quanto será gasto no novo salário.
Também apresente qual será a diferença entre o que se pagava para todos os
funcionário e o que será pago após o aumento.

'''

def mensagem(msg): 
    tam = len(msg)+4
    print('-' * tam)
    print(f' {msg}')#f para formatar a exibição..
    print('-' * tam)


def salario_aumento(porcento, sal, soma_sal):
    so = gasto_total = 0
    novo_sal = sal + sal * (porcento / 100)
    for c in range(10):
        gasto_total += novo_sal
        so = gasto_total - soma_sal
    return f'Total Novos salários R$ {gasto_total}.00' f' A diferença dos Salários Anteriores é de R$ {so}.00'

mensagem('CÁLCULO SALÁRIAL')

aumento = int(input('Porcentagem de Aumento: '))
print()
s = 0
for i in range(10):
    salario = int(input('Salário do Funcionário: R$'))
    s += salario

mensagem(f'Total Salários Antigos: R${s}.00')
mensagem(salario_aumento(aumento, salario, s))


'''

RESULTADO:

--------------------
 CÁLCULO SALÁRIAL
--------------------
Porcentagem de Aumento: 15

Salário do Funcionário: R$2600
Salário do Funcionário: R$2150
Salário do Funcionário: R$2000
Salário do Funcionário: R$3500
Salário do Funcionário: R$1900
Salário do Funcionário: R$2800
Salário do Funcionário: R$1950
Salário do Funcionário: R$2050
Salário do Funcionário: R$1950
Salário do Funcionário: R$2350
--------------------------------------
 Total Salários Antigos: R$23250.00
--------------------------------------
--------------------------------------------------------------------------------------------
 Total Novos salários R$ 27025.0.00 A diferença dos Salários Anteriores é de R$ 3775.0.00
--------------------------------------------------------------------------------------------



'''
