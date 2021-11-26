'''
(Função sem retorno sem parâmetro) Faça uma função/método que leia dois valores
positivos e apresente a soma dos N números existentes entre eles (inclusive).

Exemplo: 
    a = 2
    b = 8
    soma = 35
'''

def somar(): #Declaração da função
    a = int(input('Informe um número: '))
    b = int(input('Informe outro número: '))
    c = 0     
    for a in range(a,b+1):
      c = c + a 
      print('A Soma dos números é: ',c) #soma exibida passo a passo, até o resultado final

somar() #chamada da função

# inica em "A" .... resultado na variavel armazenada em "C" que precisa ter valor zero para iniciar 
# contagem e armazenar...



'''
# RESULTADO....

Informe um número: 2
Informe outro número: 8
A Soma dos números é:  2
A Soma dos números é:  5
A Soma dos números é:  9
A Soma dos números é:  14
A Soma dos números é:  20
A Soma dos números é:  27
A Soma dos números é:  35

'''
