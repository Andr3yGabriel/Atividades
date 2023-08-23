portas = input("Digite a posição das portas, sendo P o primeiro dígito e R o segundo: ")

if portas == "1 e 0":
    print("Caminho C")

elif portas == "0 e 1":
    print("Caminho B")

elif portas == "0 e 0":
    print("Caminho A")

elif portas == "1 e 1":
    print("Caminho C")

else:
    print("Comando inválido")