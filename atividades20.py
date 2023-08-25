try:
    distancia = int(input("Digite a distância da viagem em KM: "))

    if distancia > 0 and distancia <= 200:
        print(f'O valor da passagem será R${distancia*0.5}')

    elif distancia > 0 and distancia > 200:
        print(f'O valor da passagem será R${distancia*0.45}')

    else:
        print('Valor inválido! Tente digitar valores positivos!')

except:
    print('Operação inválida.')