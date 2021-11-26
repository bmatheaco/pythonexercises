salmin= float(input('Informe o valor do salário mínimo: '))
turno= input('Informe o seu turno (M para Matutino, V para Vespertino e N para Noturno): ')
categoria= input('Informe a sua categoria (O para Operário e G para Gerente): ')
nhrstrab= float(input('Informe a quantidade de horas trabalhadas: '))

if turno== 'M':
  coeficiente= 10/100 * salmin
if turno== 'V':
  coeficiente= 15/100 * salmin
if turno== 'N':
  coeficiente= 12/100 * salmin
 
print('O valor do Coeficiênte é:',coeficiente)
 
salbruto = nhrstrab * coeficiente
 
print('O valor do salário bruto é:',salbruto)
 
if categoria== 'O':
  if salbruto >= 300:
    imp= 5/100 * salbruto
  else:
    imp= 3/100 * salbruto
else:
  if salbruto >= 400:
    imp= 6/100 * salbruto
  else:
    imp= 4/100 * salbruto
 
print('O valor do imposto é:',imp)
 
if turno == 'N' and nhrstrab > 80:
  gratificacao= 50
else:
  gratificacao= 30
 
print('O valor da gratificação é:',gratificacao)
 
if categoria== 'O' or coeficiente <= 25:
    auxilio= 1/3 * salbruto
else:
    auxilio= 1/2 * salbruto
 
print('O valor do auxílio é de:',auxilio)
 
salliq = salbruto - imp + gratificacao + auxilio
 
print('O valor do salário liquido é de:', salliq)
 
if salliq < 350:
     print('Mal Remunerado')
if salliq >= 350 and salliq<= 600:
     print('Normal')
if salliq > 600:
     print('Bem Remunerado')
