def arm(y):
  while y > 0:
    f = f(y - 1) * y
    vb.append()
    return vb

va = []
vb = []
for x in range(1,6):
  y= int(input('Informe o {}º numero: '.format(x)))
  va.append(y)
print(arm(va))
