n1 = int(input('Digite o valor do primeiro número: '))
n2 = int(input('Digite o valor do segundo número: '))
n3 = int(input('Digite o valor do terceiro número: '))
if n1 > n2 and n1 > n3:
  print('O primeiro número é o maior')
elif n2 > n1 and n2 > n3:
  print('O segundo número é o maior')
elif n3 > n1 and n3 > n2:
  print('O terceiro número é o maior')
else:
  print('Os três números são iguais')