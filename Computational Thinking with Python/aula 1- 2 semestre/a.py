carro = []
contador = 0
for contador in range(4):
    marcas= input("Digite o nome da marca do carro: ")
    versao=  input("Digite a versão do carro: ")
    ano= int(input("Digite o ano do carro: "))
    cor= input("Digite a cor do carro: ")
    ipva= input("O IPVA do carro está pago? (S/N): ")
    carro.append([marcas, versao, ano, cor, ipva])
print(carro)