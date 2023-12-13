import random

while True:

    opcoes = ['Pedra', 'Papel', 'Tesoura']

    opcao_escolhida = random.choice(opcoes)

    jogador = input("Escolha entre Pedra, Papel ou Tesoura: ")

    if jogador == opcao_escolhida:
        print('Empate')

    elif jogador == 'Pedra' and opcao_escolhida == 'Papel':
        print(f'Computador ganhou pois escolheu {opcao_escolhida}')

    elif jogador == 'Pedra' and opcao_escolhida == 'Tesoura':
        print(f'Jogador ganhou pois a escolha do computador foi {opcao_escolhida}')

    elif jogador == 'Papel' and opcao_escolhida == 'Tesoura':
        print(f'Computador ganhou pois escolheu {opcao_escolhida}')

    elif jogador == 'Papel' and opcao_escolhida == 'Pedra':
        print(f'Jogador ganhou pois a escolha do computador foi {opcao_escolhida}')

    elif jogador == 'Tesoura' and opcao_escolhida == 'Pedra':
        print(f'Computador ganhou pois escolheu {opcao_escolhida}')

    elif jogador == 'Tesoura' and opcao_escolhida == 'Papel':
        print(f'Jogador ganhou pois a escolha do computador foi {opcao_escolhida}')

    else:
        break
