codigo = float(input("Digite o código da palestra:"))
codigo=round(codigo)
codigo=str(codigo)
match codigo:
    case '1':
        print("Palestra: Linux ")
        print("Local: Auditório 1")
    case '2':
        print("Palestra: Banco de Dados ")
        print("Local: Auditório 2")
    case '3':
        print("Palestra: Windows Server")
        print("Local: Auditório 3")
    case '4':
        print("Palestra: Lógica e Programação")
        print("Local: Auditório Principal")
    case _:
        print("Opcao Invalida")