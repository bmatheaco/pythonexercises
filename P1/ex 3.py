qhtotal=0
qmtotal=0
soma= 0
somacurso= 0

for i in range(1,7):
  qh= 0
  qm= 0
  idade= int(input('Informe a sua idade: '))
  while idade > 0:
    soma += idade
    sexo= str(input('Informe o seu sexo (M para masculino e F para feminino): '))
    if sexo == "M" or sexo == "m":
      qh += 1
    elif sexo == "F" or sexo == "f":
      qm += 1
    else:
      print('Sexo invalido')

    idade= int(input('Informe a sua idade: '))
    
  print('Existem ',qh,'homens no ',i,'º módulo')
  print('Existem ',qm,'de mulheres no ',i,'º módulo')

  qhtotal += qh
  qmtotal += qm
  
mediasidadetotal = soma/(qhtotal + qmtotal)

print('\nA media de idade de todo o curso é: ',mediasidadetotal)
print('Em todo o curso existem ',qmtotal,'mulheres e ',qhtotal,'homens')
