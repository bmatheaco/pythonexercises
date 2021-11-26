soma = 0
print('calcule e informe a média de idades de 5 alunos.')
for c in range(1,6):
    n= float(input('Insira a idade do {}º aluno: '.format(c)))
    soma += n
    media = soma/c
print('A media de idade dos 5 alunos foi de: {:} '.format(media))
