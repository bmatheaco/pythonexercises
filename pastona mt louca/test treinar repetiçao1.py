maior = 0
menor = 0
print('Insira o valor de 20 TVs')
for tv in range(1,21):
    valor= float(input('Insira o valor da {}ª TV: '.format(tv)))
    if tv == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print('O preço mais alto é: R$ {}'.format(maior))
print('O preço mais baixo é: R$ {}'.format(menor))
