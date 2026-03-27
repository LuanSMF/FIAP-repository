#6. Faça um algoritmo que solicita ao usuário dois números inteiros.
# O primeiro é o valor das horas e o
#segundo dos minutos. Verifique se a hora é válida ou inválida e
# exiba uma mensagem correspondente
#(São válidas as horas entre 00:00 e 23:59).

horas=int(input("Digite as horas: "))
minutos=int(input("Digite os minutos:"))
if(horas>=00 and horas<=23 and minutos>=00 and minutos<=59):
        print("A hora "+str(horas)+":"+str(minutos)+" é valida!")
else:
    print("A hora" + str(horas) + ":" + str(minutos) + " é invalida!")
