'''
2. Elabore uma estrutura para representar um produto (código, nome, preço).
Apliquem 10% de aumento no preço produto e apresente.

Faça o mesmo objetivo do exercício anterior utilizando VETOR/LISTA,
cadastrar 5 produtos

'''

class tipo: 
    codigo = 0
    nome = ''
    preco = 0.0
    aumento = 0.0
    valor_final = 0.0


def main(): #Principal
    lista = []
    a = tipo() #Contrutor da classe
    a.codigo.append(a(int(input('Código do Produto: ')))
    a.nome.append((input('Informe o Nome do Produto: '))
    a.preco = float(input('Informe valor do produto: '))
    print('Reajuste de 10% do valor Produto')
    a.aumento = (a.preco * 10/100)
    a.valor_final = a.preco + a.aumento
    print('Valor Final: R$ ',a.valor_final)

main()
