cont1 = 0
cont2 = 0
cont3 = 0
cont0 = 0
cont4 = 0

while True:
    voto = int(input('Digite o seu voto (1, 2, 3 - para candidatos, 0 para branco e 4 para nulo): '))

    if voto == 1:
        cont1 += 1 # cont1 = cont1 + 1
    elif voto == 2:
        cont2 += 1 
    elif voto == 3:
        cont3 += 1
    elif voto == 4:
        cont4 += 1
    elif voto == 0:
        cont0 += 1
    elif voto == -1:
        break
    else:
        print('Informe um código válido.')

if cont1 > cont2 and cont2 > cont3:
    print(f'O candidato 1 é o vencedor com {cont1} votos.')
elif cont2 > cont1 and cont1 > cont3:
    print(f'O candidato 2 é o vencedor com {cont2} votos.')
else: 
    print(f'O candidato 3 é o vencedor com {cont3} votos.')

print(f'O número de votos em branco: {cont0}')

print(f'O número de votos nulos: {cont4}')

print(f'O número de eleitores que compareceram às urnas: {cont0 + cont1 + cont2 + cont3 + cont4}')