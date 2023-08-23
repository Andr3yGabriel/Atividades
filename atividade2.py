distancia = input("Digite a distância que o robô estava da cesta: ")

if int(distancia) <= 800 and int(distancia) > 0:
    print(1)

elif int(distancia) > 800 and int(distancia) <= 1400:
    print(2)

elif int(distancia) > 1400 and int(distancia) <= 2000:
    print(3)

else:
    print("Distância fora da margem")