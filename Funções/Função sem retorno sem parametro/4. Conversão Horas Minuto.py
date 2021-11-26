'''
4. (Função sem retorno sem parâmetro) Faça uma função/método que leia um único
valor representado em segundos, converta-o e apresente o resultado em horas,
minutos e segundos.

Exemplo:
h = segundos / 3600
r = resto(segundos / 3600)
m = r / 60
s = resto(r / 60)

Observação: a hora, o minuto e o segundo devem ser apresetados como
números inteiros.

'''

def conversor():
  segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))
  
  horas = segundos // 3600
  segs_restantes = segundos % 3600
  minutos = segs_restantes // 60
  segs_restantes_final = segs_restantes % 60
  
  if horas >= 24:
    dias = horas / 24
    horas = horas % 24
    
  print( horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")

conversor()


'''
# RESULTADO....

Por favor, entre com o número de segundos que deseja converter:10000
2 horas, 46 minutos e 40 segundos.

'''
