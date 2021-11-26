alt= []
idade= []
s= 0
for i in range(5):
    alt.append(float(input('Informe a altura: ')))
    s += alt[i]

    idade.append(float(input('Informe a Idade: ')))

media= s/len(alt)
print('A Média de altura é: ',media, 'Total acumulado: ',s)

cont= 0
for i in range(5):
    if idade[i] > 25:
        cont += 1
        print('O aluno',i,' possui idade superior a 25 anos')
print('Quantidade de alunos: ',cont)
