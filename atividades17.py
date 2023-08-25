quantidade_racao = float(input("Digite a quantidade de ração em Kg: "))
quantidade_dada = float(input("Digite quanto de ração em gramas vai para cada gato por dia: "))

quantidade_quinto = (quantidade_racao*1000) - (quantidade_dada*10)

if quantidade_quinto < 0:
    print("A quantidade de ração é insuficiente")

else:
    print(f'A quantidade de ração que sobra após 5 dias é {quantidade_quinto}')