numero1 = input("Digite o primeiro número real: ")
numero2 = input("Digite o segundo número real: ")
operacao = input("Digite uma operação: ")
 
if operacao == "+":
    print(float(numero1)+float(numero2))

elif operacao == "-":
    print(float(numero1)-float(numero2))

elif operacao == "*":
    print(float(numero1)*float(numero2))

elif operacao == "/":
    print(float(numero1)/float(numero2))

else:
    print("Operação desconhecida")