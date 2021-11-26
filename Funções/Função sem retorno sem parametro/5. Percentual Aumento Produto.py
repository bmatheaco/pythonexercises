'''
5. (Função sem retorno sem parâmetro) Faça uma função/método que receba o
preço antigo e atual de um produto, determine o percentual de acréscimo entre
esses valores e apresente-o.

Exemplo:

r = (100 * preco_novo - 100 * preco_antigo) / preco_antigo

'''

def aumento(): #Declaração da função
    a = float(input('Informe o preço antigo do produto: R$ '))
    b = float(input('Informe o preço atual do produto: R$ '))
    c = (100 * b - 100 * a) / a    
    
    print('O Percentual de aumento é de: {0:.2f} '.format(c),'Porcento') 

aumento() #chamada da função



'''
# RESULTADO....

Informe o preço antigo do produto: R$ 35.00
Informe o preço atual do produto: R$ 39
O Percentual de aumento é de: 11.43  Porcento

'''
