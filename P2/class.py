class Aluno:
    matricula = 0
    nome = ''
    p1 = 0.0
    p2 = 0.0
    media = 0.0
 
def main(): #principal
    a = Aluno() # construtor da classe
    a.matricula = int(input('Informe a matrícula: '))
    a.nome = input('Informe o nome do aluno: ')
    a.p1 = float(input('Informe a nota da P1: '))
    a.p2 = float(input('Informe a nota da P2: '))
    a.media = (a.p1 + a.p2) / 2
    print(f'Média = {a.media:.2f}.')
 
main()
