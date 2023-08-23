sombra_predio = float(input("Digite o tamanho da sombra do prédio: "))
sombra_propria = float(input("Digite o tamanho da sua sombra: "))
altura_propria = float(input("Digite a sua altura: "))

altura_predio = (sombra_predio/sombra_propria)*altura_propria
print(f"A altura do prédio é {altura_predio}")