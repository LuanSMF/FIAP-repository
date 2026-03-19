matriz = [[0,0]]
soma=0
multiplicacao=1
for c in range(2):
    matriz[0][c]= int(input("Digite o seu "+ str(c+1) +"* número: "))
    soma+=matriz[0][c]
    multiplicacao*=matriz[0][c]

print(str(matriz[0][0])+"+"+str(matriz[0][1])+"="+str(soma))
print(str(matriz[0][0])+"*"+str(matriz[0][1])+"="+str(multiplicacao))