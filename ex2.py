altura = float(input('Digite a altura: '))
sexo = input('Digite o sexo: ')

pesoIdeal = 0.0
if sexo.upper() == 'M': # lower
    pesoIdeal = (72.7*altura)-58
elif sexo.upper() == 'F': 
    pesoIdeal = (62.1*altura)-44.7
else:
    print('O sexo informado deve ser M para masculino ou F para feminino.')

if pesoIdeal > 0:
    print('O sexo informado foi: ', sexo.upper())
    print('Seu peso ideal é: ', round(pesoIdeal, 2))
