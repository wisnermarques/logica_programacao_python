somaIdades = 0
cont = 0
while True:
    try:
        idade = int(input('Digite a idade (para encerrar digite zero): '))
        if idade > 0:
            somaIdades += idade
            cont += 1
        elif idade == 0:
            break
        else:
            print('Informe uma idade válida.')
    except Exception as e:
       print(f'Idade inválida: {e}')
 
mediaIdade = somaIdades / cont
print(f'A média de idades é: {mediaIdade}')