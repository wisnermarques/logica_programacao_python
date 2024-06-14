try:
    print('############# Entrada de dados #################')
    altura = float(input('Digite a altura: '))
    sexo = input('Digite o sexo: ')
    peso = float(input('Digite o seu peso: '))
except Exception as e:
    print('Houve algum erro', e)
else:
    print('\n############# Saída de dados #################')
    imc = round(peso / altura ** 2, 2)
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

    if imc < 18.5:
        print('Seu imc é: ', imc, ' - Abaixo do peso')
    elif imc < 25:
        print('Seu imc é: ', imc, ' - Peso normal')
    elif imc < 30:
        print('Seu imc é: ', imc, ' - Sobrepeso')
    elif imc < 35:
        print('Seu imc é: ', imc, ' - Obesidade grau 1')
    elif imc < 40:
        print('Seu imc é: ', imc, ' - Obesidade grau 2')
    else:
        print('Seu imc é: ', imc, ' - Obesidade grau 3')
finally:
    print('## :)Fim do programa! ##')
