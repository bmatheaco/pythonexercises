'''
4. (Função com retorno com parâmetro) Faça um programa contendo uma
função/método que receba um valor de porcentagem de aumento via parâmetro,
aplique este aumento a varios funcionários, retorne e apresente o
novo salário.

'''

def salario(p):
    lista = []
    novo_salario = sal + sal * (p / 100)
    while True:
        lista.append(novo_salario)
        for c in range(len(lista)):
            n_sal = lista[c]
        return n_sal

porcentagem = int(input(f'Porcentagem de aumento:'))
print(f'{"-"*20}')
while True:
    sal = float(input('Insira seu salário, [0] para sair: '))
    if sal == 0:
        break
    print(f'Novo Salário: R${salario(porcentagem)}\n{"-"*20}')


'''

RESULTADO:

Porcentagem de aumento:12
--------------------
Insira seu salário, [0] para sair: 2600
Novo Salário: R$2912.0
--------------------
Insira seu salário, [0] para sair: 3200
Novo Salário: R$3584.0
--------------------
Insira seu salário, [0] para sair: 1600
Novo Salário: R$1792.0
--------------------
Insira seu salário, [0] para sair: 3600
Novo Salário: R$4032.0
--------------------
Insira seu salário, [0] para sair: 0

'''
