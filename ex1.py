'''
Sistema que leia duas notas e o nome do aluno
calcular a média
mostrar resultado da média
mostrar se aluno está aprovado (media >= 6)
reprovado (media < 5 )
recuperação (media >= 5 e media < 6)

'''
nota1 = float(input('digite a nota 1: '))
nota2 = float(input('digite a nota 2: '))
media = (nota1 + nota2) / 2

print('Média: ', media)

if media >= 6:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')
