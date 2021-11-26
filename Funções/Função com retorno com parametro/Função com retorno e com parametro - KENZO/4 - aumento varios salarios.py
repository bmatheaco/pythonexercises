"""
4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de
aumento via parâmetro, aplique este aumento a VÁRIOS salárioS de funcionárioS, retorne e apresente o novo salário.
"""

def salario(p):
    lista = []
    novo_salario = sal + sal * (p / 100)
    while True:
        lista.append(novo_salario)
        for c in range(len(lista)):
            n_sal = lista[c]
        return n_sal

porcentagem = int(input(f'Porcentagem de aumento:'))
print(f'{"="*20}')
while True:
    sal = float(input('Insira seu salário, [0] para sair: '))
    if sal == 0:
        break
    print(f'Novo Salário: R${salario(porcentagem)}\n{"~"*20}')