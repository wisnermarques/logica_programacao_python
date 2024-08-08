numero =  int(input('Digite um número: '))

if numero % 3 == 0 and numero % 7 == 0:
    print(f'O {numero} é divisivel por 3 e 7')
else:
    print(f'O {numero} não é divisivel por 3 e 7')