while True:
    numero = input("Digite um número positivo: ")

    if int(numero) > 0 and int(numero)%2 == 0:
        print("Par")
    
    elif int(numero) > 0 and int(numero)%2 != 0:
        print("Ímpar")
    
    else: 
        break