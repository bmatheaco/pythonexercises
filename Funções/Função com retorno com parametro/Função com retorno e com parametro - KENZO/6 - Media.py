"""
6. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2)
calcule a média, chame outra função que avalie se este aluno esta aprovado ou reprovado retornando a str/string
'Aprovado' ou 'Reprovado'.
"""


def situacao(me):
    print(f'O aluno obteve média {me}')
    if me >= 6:
        return 'APROVADO!'
    else:
        return 'REPROVADO!'

def media(n1, n2):
    med = (n1 + n2) / 2
    return med
p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
media(p1, p2)
print('-='*20)
print(situacao(media(p1, p2)))

