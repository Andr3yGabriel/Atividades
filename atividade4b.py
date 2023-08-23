lista = []

numero1 = input("Digite o primeiro valor: ")
numero2 = input("Digite o segundo valor: ")
numero3 = input("Digite o terceiro valor: ")

lista.append(int(numero1))
lista.append(int(numero2))
lista.append(int(numero3))
lista.sort(reverse=True)
print(lista)