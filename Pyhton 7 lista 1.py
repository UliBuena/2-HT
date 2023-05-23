def inicio():
ip = float(input('Insira o índice de poluição: '))
if ip <= 0.3:
  print('Indústrias do grupo 1° devem suspender as atividades')
elif ip >= 0.4:
  print('Indústrias do grupo 1° e 2° devem suspender suas atividades')
elif ip >= 0.5:
  print('Todos os grupos devem suspender suas atividades')
else:
  print('Índice de poluição estável')
inicio()