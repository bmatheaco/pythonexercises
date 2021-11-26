A= float(input('Digite um valor para A: '))
B= float(input('Digite um valor para B: '))
C= float(input('Digite um valor para C: '))
I= float(input('Digite um valor para I: (1, 2 ou 3) '))
if I==1:
    if A<B and A<C:
        if B<C:
            print('A ordem crescente dos numeros é: ',A,"-",B,"-",C)
        else:
            print('A ordem crescente dos numeros é: ',A,"-",C,"-",B)
    if B<A and B<C:
        if A<C:
            print('A ordem crescente dos numeros é: ',B,"-",A,"-",C)
        else:
            print('A ordem crescente dos numeros é: ',B,"-",C,"-",A)
    if C<A and C<B:
        if A<B:
            print('A ordem crescente dos numeros é: ',C,"-",A,"-",B)
        else:
            print('A ordem crescente dos numeros é: ',C,"-",B,"-",A)
if I==2:
    if A>B and A>C:
        if B>C:
            print('A ordem decrescente dos numeros é: ',A,"-",B,"-",C)
        else:
            print('A ordem decrescente dos numeros é: ',A,"-",C,"-",B)
    if B>A and B>C:
        if A>C:
            print('A ordem decrescente dos numeros é: ',B,"-",A,"-",C)
        else:
            print('A ordem decrescente dos numeros é: ',B,"-",C,"-",A)
    if C>A and C>B:
        if A>B:
            print('A ordem decrescente dos numeros é: ',C,"-",A,"-",B)
        else:
            print('A ordem decrescente dos numeros é: ',C,"-",B,"-",A)
if I==3:
    if A>B and A>C:
        print('A ordem desejada é: ',B,"-",A,"-",C)
    if B>A and B>C:
        print('A ordem desejada é: ',A,"-",B,"-",C)
    if C>A and C>B:
        print('A ordem desejada é: ',A,"-",C,"-",B)