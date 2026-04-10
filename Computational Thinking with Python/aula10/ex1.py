#Uma loja fornece 10% de desconto para funcionários e
# 5% de desconto para clientes vips. Faça um programa que calcule o valor total
# a ser pago por uma pessoa. O programa deverá solicitar o valor total da compra
# efetuada e um código que identifique se o comprador é um cliente comum ("C"),
# funcionário ("F") ou vip ("V").

valor=float(input("Digite o valor total da compra:"))
client=input("Digite o tipo do comprador:")
if(client!= 'C' and client!= 'F' and client!= 'V'):
    print("ERROR")
else:
    desconto=0.1*valor
    match (client):
        case 'C':
            print("Não há desconto, valo final:",valor)
        case 'F':
            valor=valor-desconto
            print("Desconto:",desconto)
            print("valor final:", valor)
        case 'V':
            valor=valor-0.05
            print("Desconto:", desconto)
            print("valor final:", valor)
