numero = input("Digite um número: ")

if int(numero) > 0 and int(numero)%2 == 0:
    print("Este número é positivo e par")

elif int(numero) < 0 and int(numero)%2 == 0:
    print("Este número é negativo e par")

elif int(numero) > 0 and int(numero)%2 != 0:
    print("Este número é positivo e ímpar")

elif int(numero) < 0 and int(numero)%2 != 0:
    print("Este número é negativo e ímpar")