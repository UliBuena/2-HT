peso = float(input("Insira o peso do peixe: "))
es = peso - 50
mon = es * 4
if peso > 50:
    print('O valor da multa por excesso é de:', mon)
else:
    print('Não há taxa de multa')
