'''
3. Elabore uma estrutura para representar um produto (código, nome, preço).
Crie uma função para cadastrar 5 produtos. Crie outra função para
aplicar 10% de aumento no preço do produto e apresente todos os dados do preço.

'''

class produto:
   codigo = 0
   nome = ' '
   preco = 0.0
   aumento = 0
   
   

def aumento(vetP):
    for i in range(2): #Calculo aplicando aumento por produto armazenado em lista
      vetP[i].preco = vetP[i].preco + (vetP[i].preco * 10 / 100)
      print('O produto',vetP[i].nome,'de codigo',vetP[i].codigo)
      print('recebeu um aumento de 10% e passou a ser',vetP[i].preco)
    

def cadastro(vetP):
   for i in range(2): #Cadastro de produtos, armazenado em lista
      a = produto()
      a.codigo = int(input('Digite o codigo: '))
      a.nome = str(input('Digite o nome: ')).upper()
      a.preco = float(input('Digite o preco R$: '))
      vetP.append(a)
   aumento(vetP) #def aumento - aplicando
   

def main():
   vetProd = []
   vetProd = cadastro(vetProd)
   
   

main()
