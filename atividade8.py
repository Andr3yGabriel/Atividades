valor = input("Digite o valor da compra: ")
codigo = input("Digite o código da forma de pagamento: ")

if codigo == "1":
    print(f"o valor a ser pago é {float(valor) - float(valor)*0.08}")

elif codigo == "2":
    print(f"O valor a ser pago é {float(valor) - float(valor)*0.04}")

elif codigo == "3":
    print(f"O valor da compra é de duas vezes de {float(valor)/2}")

elif codigo == "4":
    print(f"O valor a ser pago é de 4 vezes de {(float(valor) + float(valor)*0.08)/4} totalizando {float(valor) + float(valor)*0.08}")

else:
    print("Código desconhecido!")