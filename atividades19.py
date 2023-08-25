try:
    velocidade = int(input("Digite a velocidade do veículo em Km/H: "))
    limite = 80

    if velocidade > 0 and velocidade > limite:
        print(f'Você foi multado no valor de R${(velocidade-limite)*5}.')

    elif velocidade > 0 and velocidade < limite:
        print('Você não foi multado.')
    
    else:
        print('Valor inválido! Certifique-se de digitar valores positivos!')

except:
    print("Valor inválido")