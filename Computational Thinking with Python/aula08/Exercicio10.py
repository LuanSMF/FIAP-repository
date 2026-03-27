#10. Faça um algoritmo que solicite o salário fixo e
# o valor das vendas efetuadas pelo vendedor de uma
#empresa. Sabendo-se que ele recebe uma comissão de 3%
# sobre o total das vendas até R$ 1.500,00
#mais 5% sobre o que ultrapassar este valor,
# calcular e escrever o seu salário total.

salario= int(input("Digite seu salario:"))
vendas= int(input("Digite o valor da vendas:"))
comissao = 0

if(vendas>1500):
    comissao= 1500*0.03
    conta = vendas-1500
    conta = conta* 0.05
    comissao = comissao + conta
else:
    comissao = vendas*0.03
total=comissao+salario
print("O salário total é: ",total)



