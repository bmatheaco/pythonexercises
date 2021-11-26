i= []
s= []
o= []
c= []
def armazenamento():
    for h in range(1,6):
        idade = int(input('Informe a idade do {}º habitante: '.format(h)))
        sexo = str(input('Informe o sexo do {}º habitante(M - masculino e F - feminino): '.format(h)))
        olho = str(input('Informe a cor dos olhos do {}º habitante(A - azuis e C - castanhos): '.format(h)))
        cabelo = str(input('Informe a cor dos cabelos do {}º habitante(L - louros, P - pretos e C - castanhos): '.format(h)))
        i.append(idade)
        s.append(sexo)
        o.append(olho)
        c.append(cabelo)

    tudo=[i, s, o, c]

    return tudo


def idadecp():
    cont = 0
    soma = 0
    for h in range(5):
        if o[h] == "c" and c[h] == "p":
            soma += i[h]
            cont += 1
    if cont > 0:
        return "A média de idade dos habitantes com olhos castanhos e cabelos pretos {}.".format(soma/cont)
    else:
        return "Não existe nenhum habitante com olhos castanhos e cabelos pretos."



def maior():
    mai = 0
    for idade in i:
        if idade > mai:
            mai = idade
        
    return "O habitante mais experiente tem {} anos de idade.".format(mai)

def barbie():
    cont = 0
    for h in range(5):
        if s[h] == "f" and i[h] >= 18 and i[h] <= 35 and o[h] == "a" and c[h] == "l":
            cont += 1

    return "Há {} habitantes do sexo feminino com idade entre 18 e 35 anos(inclusive), que tem olhos azuis e cabelos louros.".format(cont)
        


print(armazenamento())
print(idadecp())
print(maior())
print(barbie())
