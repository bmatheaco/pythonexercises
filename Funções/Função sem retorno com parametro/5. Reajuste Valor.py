'''

5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um
produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem lida.
'''

def reajuste (a,b):
   r = a + ( a * (b/100))
   print('O Reajuste do valor é de: R$ ',r)

x = float(input('Informe o valor do produto: R$ '))
z = float(input('Informe percentual de aumento: '))
reajuste (x,z)

'''
# RESULTADO....

Informe o valor do produto: R$ 100
Informe percentual de aumento: 10
O Reajuste do valor é de: R$  110.0

'''
