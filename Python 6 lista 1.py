c = None
n = None
exc = None
mont = None
monex = None
  print('Insira seu código: ')
c = input()
  print('Insira o número de horas trabalhadas: ')
n = float(input())
if n > 50:
exc = n - 50
monex = exc * 20
mont = monex * 10
  print('O valor do salário excedente é de: ', monex)
else:
  print('Não foi realizada nenhuma hora extra de trabalho')