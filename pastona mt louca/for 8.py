for a in range(1,11):
    sal= float(input('Insira o salário do {}º funcionário: '.format(a)))
    if sal <= 300:
        nsal= sal + sal * 50/100
        print('O novo salario do funcionário é: R${:.2f}'.format(nsal))
    else:
        nsal= sal + sal * 30/100
        print('O novo salário do funcionário é: R${:.2f}'.format(nsal))
