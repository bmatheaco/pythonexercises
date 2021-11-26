'''Elabore uma estrutura para representar um produto (código, nome, preço)'''

class produto:
    nome = ''
    codigo = 0
    preco = 0.0

def main():
    a = produto()
    a.nome = input('Informe o nome do produto: ')
    a.codigo = int(input('Informe o código do produto: ')
    a.preco = float(input('Informe o preço do produto: ')
    print('Produto: ', a.nome, \n
          'Código do produto: ', a.codigo,\n
          'Preço do produto: ', a.preco)
