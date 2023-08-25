nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário incluindo os valores decimais: "))

if salario > 0:
    print(f"Bom dia prezado {nome}\n")
    print(f"Seu novo salário é {salario + salario*0.25}")

else:
    print("Coloque um valor válido como salário")

if salario < 2112.01:
    print("Sua aliquota é de 0% então você não pagará impostos")

elif salario >= 2112.01 and salario < 2826.65:
    print(f"Você deverá pagar um total de {salario*0.075} de impostos")

elif salario >= 2826.66 and salario < 3751.05:
    print(f"Você deverá pagar um total de {salario*0.15} de impostos")

elif salario >= 3751.06 and salario < 4664.68:
    print(f"Você deverá pagar um total de {salario*0.225} de impostos")

elif salario > 4664.68:
    print(f"Você deverá pagar um total de {salario*0.275} de impostos")

