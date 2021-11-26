class Produto:
    codigo = 0
    nome = ''
    preco = 0.0

def main():
    vetP = []
    print('LEITURA DOS DADOS DO PRODUTO...')
    for i in range (5):
        produto = Produto()  # declaração tipo de estrutura
        #leitura da variável do tipo estrutura (Produto)
        produto.codigo = int(input('Informe o código do produto: '))
        produto.nome = input('Informe o nome do produto: ')
        produto.preco = float(input('Informe o preço do produto: '))
        produto.preco = produto.preco + produto.preco * 10/100
        vetP.append(produto)

    print('APRESENTAÇÃO DOS DADOS DO PRODUTO...')
    for i in range(5):
        print(f'Código: {vetP[i].codigo}, \tProduto: {vetP[i].nome}, \tPreço: R${vetP[i].preco}')


#chamada da função
main()
