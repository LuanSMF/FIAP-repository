salariobase=2500
comissao=200
produto =input('Digite o nome do Vendedor:')
quantidade =float(input('Digite a Quantidade de carros vendidos:'))
totalv=float(input('Digite o valor total vendido:'));
comissaoextra=0.02*totalv
comissaoporv=comissao*quantidade
salario=salariobase+comissaoextra+comissaoporv
print(salario)

