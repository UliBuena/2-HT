def inicio():
n1 = 0
valor = 1
divisor = 0
x = int(input('Digite um valor: '))
if x > 0:
while valor <= x:
if x % valor == 0:
divisor += 1
valor += 1
if divisor == 2:
  print('O número é primo')
else:
  print('O número não é primo')
else:
  print('O número é negativo ou seu valor é igual a ')
inicio()