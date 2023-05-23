import time
# Função para limpar a tela
def limpa():
print('\n' * 100)
# Função principal do programa
def inicio():
# Variáveis para contagem dos votos
lobao = 0
carlinhos = 0
altair = 0
dalva = 0
brancos = 0
nulos = 0
total_votos = 0
# Loop para receber os votos
while True:
limpa()
print('Escolha seu candidato ou digite 0 para encerrar\n')
print('1 - Lobão')
print('2 - Carlinhos')
print('3 - Altair')
print('4 - Dalva')
print('5 - Branco\n')
print('Qualquer número diferente de 0, 1, 2, 3, 4 e 5 anulará o seu voto')
voto = int(input('Digite seu voto: '))
limpa()
if voto == 1:
print('Candidato Lobão está inelegível devido a suspeita de lavagem de dinheiro')
time.sleep(2)
continue
if voto == 0:
print('Votação encerrada!\n')
break
# Contabilizando os votos
if voto == 1:
lobao += 1
elif voto == 2:
carlinhos += 1
elif voto == 3:
altair += 1
elif voto == 4:
dalva += 1
elif voto == 5:
brancos += 1
else:

nulos += 1
total_votos = lobao + carlinhos + altair + dalva + brancos +
nulos
# Calculando as porcentagens
if total_votos > 0:
porcentagemlobao = (lobao * 100.0) / total_votos
porcentagemcarlinhos = (carlinhos * 100.0) / total_votos
porcentagemaltair = (altair * 100.0) / total_votos
porcentagemdalva = (dalva * 100.0) / total_votos
porcentagem_brancos = (brancos * 100.0) / total_votos
porcentagem_nulos = (nulos * 100.0) / total_votos
print('\nTotal de votos: ', total_votos, '\n')
print('Lobão: ', lobao, ' voto(s). ', porcentagemlobao, '% do total')
print('Carlinhos: ', carlinhos, ' voto(s). ', porcentagemcarlinhos, '% do total')
print('Altair: ', altair, ' voto(s). ', porcentagemaltair, '% do total')
print('Dalva: ', dalva, '' voto(s). '', porcentagemdalva, '% do total')
print('Brancos: ', brancos, ' voto(s). ', porcentagem_brancos, '% do total')
print('Nulos: ', nulos, ' voto(s). ', porcentagem_nulos