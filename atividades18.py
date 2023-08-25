primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input("Digite a razão da PA: "))
numero_termos = 10

print(f"Os 10 primeiros termos da progressão aritmética são:")
for n in range(1, 11):  
    an = primeiro_termo + (n - 1) * razao
    print(an)

soma = (numero_termos/2) * (primeiro_termo + (primeiro_termo + (numero_termos - 1) * 10))

print(f'A soma dos termos dessa PA é: {soma}')