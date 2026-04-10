#Faça um algoritmo que verifica se um número inteiro informado pelo
# usuário é múltiplo de 3, utilizando o match-case.
num = float(input("Digite um numero:"))
num=round(num)
match (num%3==0):
        case'0':
            print(f'O numero {num} é multiplo de 3')
        case _:
            print(f'O numero {num} não é multiplo de 3')
