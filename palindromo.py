palavra = input('Digite a palavra: ')
palavramod = palavra.replace(' ', '')
if palavramod == palavramod[::-1]:
    print(f'A palavra {palavra} é um palindromo')

else:
    print('nao é palindromo')