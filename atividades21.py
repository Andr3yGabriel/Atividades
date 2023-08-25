celsius = int(input('Digite o valor da temperatura em Celsius: '))

conversao_kelvin = celsius+273.15
conversao_fahrenheit = (celsius*1.8) + 32
conversao_rankine = (celsius*1.8) + 491.67

print('As temperaturas relativas a essa temperatura em celsius são:')
print(f'{conversao_kelvin} Kelvin, {conversao_fahrenheit}° Fahrenheit e {conversao_rankine}° Rankine')