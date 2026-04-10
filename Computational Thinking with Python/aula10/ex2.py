#2. Faça um programa que receba um número, digitado pelo usuário
# e mostre o menu para selecionar o tipo de cálculo que deve ser realizado.
# Exiba o resultado do cálculo efetuado.

#1 - O dobro
#2 - A metade
#3 - 10% do número

num = int(input("Digite um numero:"))
num=round(num)
num=str(num)
match (num):
    case '1':
        num=int(num)
        resultado=num*2
        print(f" O dobro de {num} é = {resultado}")
    case '2':
        num = int(num)
        resultado=num/2
        print(f" A metade de {num} é = {resultado}")
    case '3':
        num = int(num)
        resultado = num *0.1
        print(f" 10% de {num} é = {resultado}")