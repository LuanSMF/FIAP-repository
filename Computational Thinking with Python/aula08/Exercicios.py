#
#Faça um algoritmo que solicita ao usuário as notas de três provas. Calcule a média aritmética e
#informe se o aluno foi Aprovado ou Reprovado (o aluno é considerado aprovado com a média igual
#ou superior a 6).
#

nota= int(input("Digite a nota :"))
nota1= int(input("Digite a nota :"))
nota2= int(input("Digite a nota: "))
soma= nota+nota1+nota2
media=soma/3
if(media>=6):
    print("Aluno aprovado")
else:
    print("Aluno Reprovado")
