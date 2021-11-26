'''

10. (Função sem retorno com parâmetro) Faça uma função/método para verificar
e contar quantas letras a tem numa frase.

'''
def verifica_caracteres(texto,char):
    cont = 0
    for letra in texto:
        if letra == char:
            cont += 1
    print('Letra -',char,": apareceu",cont,"vezes na string")
    
string=input("Digite um texto qualquer: ")
caractere = input("Qual caractere deseja pesquisar: ")
print()

verifica_caracteres(string,caractere)

'''
# RESULTADO....

Digite um texto qualquer: vamos fazer a atividade na sala de aula
Qual caractere deseja pesquisar: a

Letra - a : apareceu 10 vezes na string

'''
