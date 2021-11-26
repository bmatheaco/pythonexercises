soma= 0
media= 0
sal= 0

sal= float(input('Informe o salário do funcionário: '))

while sal > 0:
    aumento = (sal * 10/100)+ aumento
    media = media + aumento
    soma += 1
    print('O seu novo salário é: ',aumento)

    sal= float(input('Informe um outro salário: '))

media = media/soma
print('A média dos salários é de: ',media)
