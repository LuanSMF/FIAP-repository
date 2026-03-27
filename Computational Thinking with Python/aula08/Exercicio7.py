#7. Faça um algoritmo que solicite dois números ao
# usuário e exiba apenas o maior deles. Caso eles sejam
#iguais exiba a mensagem “Números Iguais”.

numero=int(input("Digite um número:"))
numero2=int(input("Digite um número:"))

maior=0
if(numero>numero2):
    maior=numero
else:
    maior=numero2

print("O maior numero é: "+str(maior))