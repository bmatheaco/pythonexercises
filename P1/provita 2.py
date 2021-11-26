def inss(sal):
    if sal <= 1045:
        return sal*0.075
    elif sal >= 1045.01 and sal <= 2089.6:
        return sal*0.09
    elif sal >= 2089.61 and sal <= 3134.4:
        return sal*0.12
    elif sal >= 3134.41 and sal <= 6101.06:
        return sal*0.14
    else:
        return 713.1

def ir(sal):
    if sal <= 1903.98:
        return 0
    elif sal >= 1903.99 and sal <= 2826.65:
        return (sal*0.075) - 142.80
    elif sal >= 2826.66 and sal <= 3751.05:
        return (sal*0.15) - 354.80
    elif sal >= 3751.06 and sal <= 4664.68:
        return (sal*0.225) - 636.13
    else:
        return (sal*0.275) - 869.36


for k in range(1,11):
    sal= float(input('Informe o {}º salário: R$ '.format(k)))
    print('O valor do INSS será: R$ {:.2f}'.format(inss(sal)))
    dpsinss = sal - inss(sal)
    print('O valor do IR será: R$ {:.2f}'.format(ir(dpsinss)))
    valorfinal = sal - inss(sal) - ir(dpsinss)
    print('O salário líquido ficou: R$ {:.2f}'.format(valorfinal))
