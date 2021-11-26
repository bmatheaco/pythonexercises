def oo(n):

  s = 0
  for i in range(1, n):
    if n % i == 0:
      s += i
  if s == n:
    return True
  else:
    return False

def perfc():
  n = int(input('Verificar de 1 há:  '))
  z = []
  for i in range(1, n + 1):
    if(oo(i)):
      z.append(i)
  print(z)
  if len(z) > 3:
    print(z[0,1,2,3])


perfc()
