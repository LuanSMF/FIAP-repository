#3. Faça um algoritmo que solicita ao usuário um número inteiro e exiba este número na tela. Se o
#número for negativo, antes de ser exibido, ele deve ser transformado no equivalente positivo.

numero=int(input("Digite um numero:"))
inverso=0

if(numero<=0):
    inverso=numero*(-1)

print("Você Digitou: ", inverso)