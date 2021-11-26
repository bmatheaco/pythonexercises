print('MENU DE OPÇÕES')
print('1 - IMPOSTO')
print('2 - NOVO SALÁRIO')
print('3 - CLASSIFICAÇÃO')
operacao= int(input('DIGITE A OPÇÃO DESEJADA: '))
if operacao == 1:
  sal= float(input('Digite seu salário: '))
  if sal < 500:
    imp = sal * 5/100
  if sal >= 500 and sal <= 850:
    imp = sal * 10/100
  if sal > 850:
      imp = sal * 15/100
      print('A taxa do imposto é:',imp)

if operacao == 2:
  sal= float(input('Digite seu salário: '))
  if sal > 1500:
    aumento = 25
  if sal >= 750 and sal <= 1500:
    aumento = 50
  if sal >= 450 and sal < 750:
    aumento = 75
  if sal < 450:
    aumento = 100
  novosal = sal + aumento
  print= ('O seu novo salário é:', novosal)

if operacao == 3:
  sal= float(input('Digite seu salário: '))
  if sal <= 700:
    print('Mal Remunerado')
  if sal > 700:
    print('Bem Remunerado')
elif operacao < 1 or operacao > 3:
  print('Opção Inválida!')