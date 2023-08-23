alunos = input("Digite quantos alunos irão para a exursão: ")

monitores = input("Digite quantos monitores irão para a excursão: ")

total = int(alunos) + int(monitores)

if int(total) <= 50:
    print("Somente uma viagem será necessária!")

else:
    print("Será necessária mais que uma viagem!")