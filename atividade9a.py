from math import sqrt

cateto1 = int(input("Digite o valor do primeiro cateto: "))
cateto2 = int(input("Digite o valor do segundo cateto: "))

hipotenusa = sqrt((cateto1)**2 + (cateto2)**2)

print(f"O valor da hipotenusa é {hipotenusa}")