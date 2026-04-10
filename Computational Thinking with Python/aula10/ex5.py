
print("CODIGO 1 | PRATO - PICANHA | VALOR R$25.00")
print("CODIGO 2 | PRATO - LASANHA | VALOR R$20.00")
print("CODIGO 3 | PRATO - Strogonoff | VALOR R$20.00")
print("CODIGO 4 | PRATO - BIFE ACEBOLADO | VALOR R$15.00")
print("CODIGO 5 | PRATO - PÃO COM OVO | VALOR R$5.00")

prato = int(input("Digite seu prato:"))
opcao = input("Aceita pagar uma taxa de Serviço?")

match prato:

    case '1':
        valor=25
        match opcao:
            case "S":
                taxa =valor*0.1
                valor=valor+taxa
                print(f"A taxa de serviço é de R${taxa}")
                print(f"Total: {valor}")
            case"N":
                print(f"Total: {valor}")
    case '2':
        valor=20
        match opcao:
            case "S":
                taxa = valor * 0.1
                valor = valor + taxa
                print(f"A taxa de serviço é de R${taxa}")
                print(f"Total: {valor}")
            case "N":
                print(f"Total: {valor}")
    case '3':
        valor=20
        match opcao:
            case "S":
                taxa = valor * 0.1
                valor = valor + taxa
                print(f"A taxa de serviço é de R${taxa}")
                print(f"Total: {valor}")
            case "N":
                print(f"Total: {valor}")
    case '4':
        valor=5
        match opcao:
            case "S":
                taxa = valor * 0.1
                valor = valor + taxa
                print(f"A taxa de serviço é de R${taxa}")
                print(f"Total: {valor}")
            case "N":
                print(f"Total: {valor}")
    case '5':
        valor=15
        match opcao:
            case "S":
                taxa = valor * 0.1
                valor = valor + taxa
                print(f"A taxa de serviço é de R${taxa}")
                print(f"Total: {valor}")
            case "N":
                print(f"Total: {valor}")
