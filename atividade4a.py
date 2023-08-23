numero1 = input("Digite o primeiro valor: ")
numero2 = input("Digite o segundo valor: ")
numero3 = input("Digite o terceiro valor: ")

if int(numero1) > int(numero2) and int(numero1) > int(numero3):
    print(numero1)

elif int(numero2) > int(numero1) and int(numero2) > int(numero3):
    print(numero2)

elif int(numero3) > int(numero1) and int(numero3) > int(numero2):
    print(numero3)