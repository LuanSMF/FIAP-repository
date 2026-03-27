##8. Faça um algoritmo que solicita ao usuário
# três números e exibe na tela apenas o menor deles, ou uma
#mensagem informando que os números são iguais.


numero=int(input("Digite um número:"))
numero2=int(input("Digite um número:"))
numero3=int(input("Digite um número:"))

menor=0
if(numero<numero2 and numero<numero3):
    menor=numero
elif(numero2<numero and numero2<numero3):
    menor=numero2
elif(numero3<numero and numero3<numero2):
    menor=numero3
else:
    print("Todos os números são zero!")

print("O menor numero é: "+str(menor))