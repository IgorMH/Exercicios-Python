from random import randint

lista = []

alvo = int(input('Digite o numero buscado: '))
qe = int(input('Digite a quantidade de elementos da lista: '))
for i in range(qe):
    lista.append(randint(100, 9999))

for index in range(0, qe):
    if alvo == lista[index]:
        print(f'O numero {alvo} está no posição {lista.index(alvo)}')
        break
    else:
        print(-1)
        break