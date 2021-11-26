'''
8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora
de início e de término de um jogo, ambas divididas em dois valores distintos:
hora e minuto. Deverá ser apresentado a duração expressa em minutos,
considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele
pode começar em um dia e terminar no outro.


EXEMPLO:

se m_f < m_i
    m_f = m_f + 60
    h_f = h_f - 1
se h_f < h_i
    h_f = h_f + 24
tot_m = m_f - m_i
tot_h = h_f - h_i
total = tot_h * 60 + tot_m

'''


def jogo():

  print('- Informe o Horario de Inicio do Jogo')
  H_inicial= int(input('Digite a Hora: '))
  M_inicial=int(input('Digite o Minuto: '))

  print()
  print('- Informe o Horario de Termino do Jogo')
  H_final=int(input('Informe a Hora : '))
  M_final=int(input('Informe o Minuto: '))

  if M_final < M_inicial:
   M_final = M_final + 60
   H_final = H_final - 1
  
  if H_final < H_inicial:
   H_final = H_final + 24
  
  Total_M = M_final - M_inicial
  Total_H = H_final - H_inicial
  Total = Total_H * 60 + Total_M
  
  print()
  print('O Jogo Durou: ',Total, 'Minutos')


jogo()


'''
# RESULTADO....

- Informe o Horario de Inicio do Jogo
Digite a Hora: 18
Digite o Minuto: 10

- Informe o Horario de Termino do Jogo
Informe a Hora : 21
Informe o Minuto: 45

O Jogo Durou:  215 Minutos

'''
