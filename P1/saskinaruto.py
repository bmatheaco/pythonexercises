idade= []
sexo= []
olho= []
cabelo= []

for h in range(1,3):
    idade.append(int(input('Informe a idade do {}º habitante: '.format(h))))
    sexo.append(str(input('Informe o sexo do {}º habitante(M - masculino e F - feminino): '.format(h))))
    olho.append(str(input('Informe a cor dos olhos do {}º habitante(A - azuis e C - castanhos): '.format(h))))
    cabelo.append(str(input('Informe a cor dos cabelos do {}º habitante(L - louros, P - pretos e C - castanhos): '.format(h))))


def i(idade):
  l=0
  if olho == "c" and cabelo == "p":
    return True
  else:
    return False

    if True:
        l = l + idade
    else:
        print ('nada ver irmao')

    media = l / 2

print("A media das idades das pessoas com olhos castanhos e cabelos pretos é: ", i(idade))
