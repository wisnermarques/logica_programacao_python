idade = int(input('Digite a idade: '))

if idade < 16:
    print(f'Idade: {idade} - Não eleitor')
elif idade >= 18 and idade <= 65:
    print(f'Idade: {idade} - Eleitor obrigatório')
else:
    print(f'Idade: {idade} - Eleitor facultativo')