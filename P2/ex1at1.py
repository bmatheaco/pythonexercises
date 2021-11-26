class Aumento:
    codigo = 0
    nome = ''
    preco = 0.0
    aumento = 0.0

def main():
    p = Aumento()
    p.codigo = int(input('Informe o código do produto: '))
    p.nome = str(input('Informe o nome do produto: '))
    p.preco = float(input('Informe o preço do produto: R$ '))
    p.aumento = (p.preco*0.1) + p.preco
    print(f'valor com aumento = R$ {p.aumento:.2f}.')

main()
