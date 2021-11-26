'''

4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de
um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%.

'''

def reajuste (x):
   a = x * (9/100)
   print('O Reajuste do valor é de: R$ ',a + x)

p = float(input('Informe o valor do produto: R$ '))

reajuste(p)

'''
# RESULTADO....

Informe o valor do produto: R$ 10
O Reajuste do valor é de: R$  10.9

'''
