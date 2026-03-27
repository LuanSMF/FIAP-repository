
#9. Faça um algoritmo que solicita ao usuário três valores
# correspondentes aos lados de um triângulo.
#Informe se o triângulo é equilátero (possui 3 lados iguais),
# isósceles (possui dois lados iguais) ou
#escaleno (não possui lados iguais)

lado = int(input("Digite um lado:"))
lado2 = int(input("Digite um lado:"))
lado3 = int(input("Digite um lado:"))

if(lado == lado2 == lado3):
    print("O tringulo é equilátero")
elif(lado == lado2 or lado==lado3 or lado2==lado3):
    print("O tringulo é isósceles")
else:
    print("O tringulo é escaleno")