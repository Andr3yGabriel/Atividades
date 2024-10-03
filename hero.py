exp = int(input('Quanto de experiência você tem? '))
personagem = input('Qual é o seu personagem? ')
nivel = ''

if exp <= 1000:
    nivel = 'ferro'
elif exp <= 2000:
    nivel = 'bronze'
elif exp <= 5000:
    nivel = 'prata'
elif exp <= 7000:
    nivel = 'ouro'
elif exp <= 8000:
    nivel = 'platina'
elif exp <= 9000:
    nivel = 'Ascendente'
elif exp <= 10000:
    nivel = 'Imortal'
else:
    nivel = 'Radiante'
    
print(f"O herói de nome {personagem} é de nível {nivel}")