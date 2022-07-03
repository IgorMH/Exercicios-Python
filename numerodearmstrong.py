numero = input('Digite o numero: ')
numero_de_digitos = len(numero)
total = 0
for i in numero:
    total = total + (int(i) ** numero_de_digitos)

if total == int(numero):
    print(f'{numero} é um numero de Armstrong')

else:
    print('não é')
