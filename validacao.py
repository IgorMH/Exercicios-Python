# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
salario = int(input('Digite o salario: '))
sexo = input('Digite o sexo: ')
estado_civil = input('Digite o estado civil: ')

if len(nome) <= 3:
    print('Nome muito curto')

if idade <= 0 or idade >= 150:
    print('Idade invalida')

if salario <= 0:
    print('Salario invalido')

if sexo != 'f' and sexo != 'm':
    print('Sexo invalido')

if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print('Estado civil invalido')