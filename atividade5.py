from math import sqrt

ponto1x = input("Digite a coordenada x do ponto 1: ")
ponto1y = input("Digite a coordenada y do ponto 1: ")
ponto2x = input("Digite a coordenada x do ponto 2: ")
ponto2y = input("Digite a coordenada y do ponto 2: ")

distancia = sqrt((float(ponto1x)-float(ponto1y))**2 + (float(ponto2x)-float(ponto2y))**2)
print(distancia)