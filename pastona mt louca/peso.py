sexo=input('informe o sexo: ')
altura= float(input('informe sua altura: '))
if sexo == 'M' or sexo == 'm' or sexo== 'masculino' or sexo== 'Masculino' or sexo== 'homem' or sexo== 'Homem':
    pesoideal= (72.7*altura)- 58
if sexo == 'F' or sexo== 'f' or sexo== 'feminino' or sexo== 'Feminino':
    pesoideal= (62.1*altura)- 44.7
print ('Seu peso ideal deveria ser= ',pesoideal)
