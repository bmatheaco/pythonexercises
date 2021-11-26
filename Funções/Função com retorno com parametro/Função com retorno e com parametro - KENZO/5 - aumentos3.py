"""
5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de
aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal do programa,
na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar
o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto
no novo salário.
Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.
"""


def salario_aumento(porcento, sal, soma_sal):
    so = gasto_total = 0
    novo_sal = sal + sal * (porcento / 100)
    for c in range(10):
        gasto_total += novo_sal
        so = gasto_total - soma_sal
    return f'Soma dos novos salários R${gasto_total}' f' A diferença é de R${so}'


aumento = int(input('Porcentagem de aumento: '))
s = 0
for i in range(10):
    salario = int(input('Salário do Funcionário: '))
    s += salario
print(f'Soma dos salários antigos: {s}\n{"="*60}')
print(salario_aumento(aumento, salario, s))
