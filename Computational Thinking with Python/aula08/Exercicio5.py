#5. Faça um algoritmo que solicita um número inteiro e exibe uma mensagem
# indicando se ele é positivo,
#negativo ou zero.

numero= int(input("Digite um número:"))
if(numero<0):
    print("O numero "+str(numero)+" é negativo")
elif(numero>0):
    print("O numero "+str(numero)+" é positivo")
else:
    print("O numero " + str(numero)+ " é zero")