#4. Faça um algoritmo que solicita ao usuário uma letra e
# exiba uma mensagem informando se é uma
#vogal ou uma consoante.

letra = input("Informe uma letra:")
vogais = "aeiouAEIOU"

if letra in vogais:
    print("Vogal")
else:
    print("Consoante")