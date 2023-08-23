lista = []

codigo = input("Digite o número de matrícula do aluno: ")
nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")

lista.append(int(nota1))
lista.append(int(nota2))
lista.append(int(nota3))
lista.sort(reverse=True)
lista[0]*=4
lista[1]*=3
lista[2]*=3

print(lista)

media = (lista[0] + lista[1] + lista[2]) / 10

if media >= 5:
    print(codigo)
    print(f"As notas foram: {nota1}, {nota2}, {nota3}")
    print(media)
    print("Aluno aprovado")

else:
    print("Aluno reprovado")