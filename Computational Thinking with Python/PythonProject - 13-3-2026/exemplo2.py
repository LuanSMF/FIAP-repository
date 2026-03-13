nome = input("Informe seu nome")
idade = int(input("Informe sua idade"))
altura = float(input("Informe sua altura:"))

print("O seu nome é", nome, "e sua idade é de", idade, "anos")
print(f"O seu nome é {nome} e sua idade é de {idade} anos")
print("O seu nome é {} e sua idade é de {} anos". format(nome,idade))

print(f"O seu nome é {nome}")
print(f"A sua idade é {idade} anos")
print(f"A sua altura é {altura} metros")

print(f"O seu nome é {nome}\nA sua idade é {idade}\n A sua altura é {altura}")