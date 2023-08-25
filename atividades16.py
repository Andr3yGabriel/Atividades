cliente = input('Digite seu nome: ')
valor_casa = int(input(f'Bem vindo senhor(a) {cliente}, digite o valor do imóvel: '))
valor_salario = int(input(f'Prezado senhor(a) {cliente}, digite o valor do seu salário: '))
periodo = int(input(f'Digite em quantos anos você deseja pagá-lo, senhor(a) {cliente}: '))

aprovado = (valor_casa/(periodo*12)) <= (valor_salario + valor_salario*0.30)
negado = (valor_casa/(periodo*12)) > (valor_salario + valor_salario*0.30)

if aprovado:
    print(f'Parabéns senhor(a) {cliente}, seu empréstimo está aprovado')

elif negado:
    print(f'Infelizmente seu empréstimo foi negado, senhor(a) {cliente}')