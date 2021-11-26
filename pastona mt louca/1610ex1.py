par = 0
impar = 0
n = int(input('Informe um número: '))
while n >= 0:
    if n%2 == 0 and n > 0:
        par += 1
    elif n%2 != 0 and n > 0:
        impar += 1
    n = int(input('Informe outro numero: '))
print('A quantidade de numeros pares é: ',par)
print('A quantidade de numeros impares é: ',impar)
